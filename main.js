document.addEventListener('DOMContentLoaded', () => {

  const canvas = document.getElementById('webgl-fluid-canvas');
  if (canvas && typeof THREE !== 'undefined') {
    const scene = new THREE.Scene();
    const camera = new THREE.OrthographicCamera(-1, 1, 1, -1, 0, 1);
    const renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true });
    
    function resize() {
      renderer.setSize(window.innerWidth, window.innerHeight);
      renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    }
    window.addEventListener('resize', resize);
    resize();

    const geometry = new THREE.PlaneGeometry(2, 2);
    
    // Load the exact image from the local folder (or base64 if running locally without a server to avoid CORS)
    const textureLoader = new THREE.TextureLoader();
    const bgTexture = textureLoader.load(typeof bgBase64 !== 'undefined' ? bgBase64 : 'assets/hero_background.png');
    
    const material = new THREE.ShaderMaterial({
      transparent: true,
      uniforms: {
        u_time: { value: 0.0 },
        u_resolution: { value: new THREE.Vector2(window.innerWidth, window.innerHeight) },
        u_mouse: { value: new THREE.Vector2(0.5, 0.5) },
        u_scroll: { value: 0.0 },
        u_image: { value: bgTexture }
      },
      vertexShader: `
        varying vec2 vUv;
        void main() {
          vUv = uv;
          gl_Position = vec4(position, 1.0);
        }
      `,
      fragmentShader: `
        uniform float u_time;
        uniform vec2 u_resolution;
        uniform vec2 u_mouse;
        uniform float u_scroll;
        uniform sampler2D u_image;
        varying vec2 vUv;

        // Simplex 2D noise
        vec3 mod289(vec3 x) { return x - floor(x * (1.0 / 289.0)) * 289.0; }
        vec2 mod289(vec2 x) { return x - floor(x * (1.0 / 289.0)) * 289.0; }
        vec3 permute(vec3 x) { return mod289(((x*34.0)+1.0)*x); }
        float snoise(vec2 v) {
          const vec4 C = vec4(0.211324865405187, 0.366025403784439, -0.577350269189626, 0.024390243902439);
          vec2 i  = floor(v + dot(v, C.yy) );
          vec2 x0 = v -   i + dot(i, C.xx);
          vec2 i1;
          i1 = (x0.x > x0.y) ? vec2(1.0, 0.0) : vec2(0.0, 1.0);
          vec4 x12 = x0.xyxy + C.xxzz;
          x12.xy -= i1;
          i = mod289(i);
          vec3 p = permute( permute( i.y + vec3(0.0, i1.y, 1.0 )) + i.x + vec3(0.0, i1.x, 1.0 ));
          vec3 m = max(0.5 - vec3(dot(x0,x0), dot(x12.xy,x12.xy), dot(x12.zw,x12.zw)), 0.0);
          m = m*m; m = m*m;
          vec3 x = 2.0 * fract(p * C.www) - 1.0;
          vec3 h = abs(x) - 0.5;
          vec3 ox = floor(x + 0.5);
          vec3 a0 = x - ox;
          m *= 1.79284291400159 - 0.85373472095314 * ( a0*a0 + h*h );
          vec3 g;
          g.x  = a0.x  * x0.x  + h.x  * x0.y;
          g.yz = a0.yz * x12.xz + h.yz * x12.yw;
          return 130.0 * dot(m, g);
        }
        // Helper to get fluid height for normal calculation
        float getFluid(vec2 p, float t, float dist) {
          vec2 q = vec2(snoise(p + t + dist), snoise(p + vec2(5.2, 1.3) + t * 0.8));
          return snoise(p + q * 2.5 + t);
        }

        void computeFluidColor(out vec3 color, vec2 st, float t, float distortion) {
          vec2 p = st * 1.5; // Large folds
          float h0 = getFluid(p, t, distortion * 2.0);
          
          // Sample neighbors to compute normal
          float e = 0.02;
          float hx = getFluid(p + vec2(e, 0.0), t, distortion * 2.0);
          float hy = getFluid(p + vec2(0.0, e), t, distortion * 2.0);
          
          vec3 normal = normalize(vec3(h0 - hx, h0 - hy, 0.1));
          
          // Lighting vectors
          vec3 lightDir = normalize(vec3(0.5, 0.8, 0.5));
          vec3 viewDir = vec3(0.0, 0.0, 1.0);
          vec3 halfVector = normalize(lightDir + viewDir);
          
          // Diffuse and Specular components
          float diffuse = max(dot(normal, lightDir), 0.0);
          float specular = pow(max(dot(normal, halfVector), 0.0), 32.0);
          
          // Royal Blue Satin Palette
          vec3 deepBlue = vec3(0.0, 0.02, 0.3);
          vec3 midBlue = vec3(0.0, 0.2, 0.9);
          vec3 brightCyan = vec3(0.3, 0.8, 1.0);
          
          // Base color mapped to height
          float f = h0 * 0.5 + 0.5;
          vec3 baseColor = mix(deepBlue, midBlue, smoothstep(0.1, 0.7, f));
          
          // Apply diffuse shading and sharp specular highlights
          color = mix(baseColor, brightCyan, diffuse * 0.5);
          color += brightCyan * specular * 0.8;
        }

        void main() {
          vec2 st = gl_FragCoord.xy / u_resolution.xy;
          st.x *= u_resolution.x / u_resolution.y;

          // Mouse push distortion (extremely subtle)
          vec2 mouse = vec2(u_mouse.x, u_mouse.y);
          float dist = distance(vUv, mouse);
          float distortion = smoothstep(0.5, 0.0, dist) * 0.05;

          // Almost imperceptible domain warp to make the image breathe slowly
          float t = u_time * 0.015;
          vec2 warpedUv = vUv;
          warpedUv.x += snoise(st * 1.5 + t) * 0.003 + distortion;
          warpedUv.y += snoise(st * 1.8 - t) * 0.003 + distortion;

          // Sample the image and animate it with the warped UVs (distortion)
          vec3 color = texture2D(u_image, warpedUv).rgb;
          // Dissolve based on scroll parallax (Ink Splatter Effect)
          // Lower frequency for large ink blobs
          float dissolveNoise = snoise(st * 3.0 + u_time * 0.05);
          // Higher frequency for smaller droplets and jagged edges
          float dissolveNoise2 = snoise(st * 10.0 - u_time * 0.1);
          float dissolveNoise3 = snoise(st * 25.0 + u_time * 0.15);
          
          // Combine noise with a bias towards large blobs but sharp details
          float combinedNoise = dissolveNoise * 0.6 + dissolveNoise2 * 0.3 + dissolveNoise3 * 0.1;
          
          float stY = gl_FragCoord.y / u_resolution.y; // 0 at bottom, 1 at top
          
          // As u_scroll increases from 0 to 1, the boundary moves from below the screen up to the top
          float boundary = mix(-0.2, 1.2, u_scroll);
          
          // Noise amplitude grows with scroll to create the splatter reach
          float edgeNoise = combinedNoise * 0.4 * smoothstep(0.0, 0.1, u_scroll);
          
          // Extremely sharp smoothstep for a hard, stark ink-like edge
          float alpha = smoothstep(boundary - 0.005, boundary + 0.005, stY + edgeNoise);

          gl_FragColor = vec4(color, alpha);
        }
      `
    });
    
    const mesh = new THREE.Mesh(geometry, material);
    scene.add(mesh);

    let targetMouse = new THREE.Vector2(0.5, 0.5);
    let currentMouse = new THREE.Vector2(0.5, 0.5);
    
    const hero = document.querySelector('.hero');
    if (hero) {
      hero.addEventListener('mousemove', (e) => {
        targetMouse.x = e.clientX / window.innerWidth;
        targetMouse.y = 1.0 - (e.clientY / window.innerHeight);
      });
      hero.addEventListener('mouseleave', () => {
        targetMouse.x = 0.5;
        targetMouse.y = 0.5;
      });
    }

    const transitionWrapper = document.querySelector('.transition-wrapper');
    const heroText = document.querySelector('.hero-center-text');
    const heroBottomText = document.querySelector('.hero-bottom-text');
    
    window.addEventListener('scroll', () => {
      // Normal scroll progression: 0 at top, 1 when scrolled exactly one screen height
      let progress = window.scrollY / window.innerHeight;
      progress = Math.max(0, Math.min(1.2, progress));
      material.uniforms.u_scroll.value = progress;
      
      if (heroText) {
        heroText.style.opacity = 1.0 - (progress * 2.5);
      }
      if (heroBottomText) {
        heroBottomText.style.opacity = 1.0 - (progress * 5.0);
      }
    });

    const clock = new THREE.Clock();

    function animate() {
      requestAnimationFrame(animate);
      currentMouse.lerp(targetMouse, 0.05);
      material.uniforms.u_time.value = clock.getElapsedTime();
      material.uniforms.u_resolution.value.set(window.innerWidth, window.innerHeight);
      material.uniforms.u_mouse.value.copy(currentMouse);
      renderer.render(scene, camera);
    }
    animate();
  }

  const liquidOverlay = document.querySelector('.liquid-overlay');
  
  // Transition wrapper logic handled in WebGL section now

  // --- Scroll Reveal System ---
  const revealElements = document.querySelectorAll('.reveal-up, .reveal-fade, .blur-reveal, .reveal-line, .slide-reveal-mask');
  
  const revealOptions = {
    threshold: 0.05, // Trigger when 5% of the element is visible
    rootMargin: "0px 0px 100px 0px" // Trigger slightly before it enters the viewport
  };

  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in-view');
        // Optional: stop observing once revealed so it doesn't animate out when scrolling up
        // observer.unobserve(entry.target); 
      }
    });
  }, revealOptions);

  revealElements.forEach(el => {
    revealObserver.observe(el);
  });

  // --- Sticky Scroll Pathways System (Wipe Reveal) ---
  
  // Mobile DOM Rearrangement for Pathways
  if (window.innerWidth <= 900) {
    const blocks = document.querySelectorAll('.pathway-content-block');
    blocks.forEach(block => {
      const visualId = block.getAttribute('data-visual');
      if (visualId) {
        const visual = document.getElementById(visualId);
        if (visual) {
          // Insert the visual at the very beginning of the block
          block.insertBefore(visual, block.firstChild);
        }
      }
    });
  }

  const pathwayBlocks = document.querySelectorAll('.pathway-content-block');
  const pathwayVisuals = document.querySelectorAll('.pathways-visuals .pathway-shape-container');

  if (pathwayBlocks.length > 0 && pathwayVisuals.length > 0) {
    function updateWipes() {
      for (let i = 1; i < pathwayBlocks.length; i++) {
        const block = pathwayBlocks[i];
        const visual = pathwayVisuals[i];
        if (!block || !visual) continue;

        const blockRect = block.getBoundingClientRect();
        // Calculate visual's top edge on screen assuming it's vertically centered in 100vh
        const visualHeight = visual.offsetHeight;
        const visualTop = (window.innerHeight - visualHeight) / 2;

        let localY = blockRect.top - visualTop;
        localY = Math.max(0, Math.min(visualHeight, localY));

        visual.style.clipPath = `inset(${localY}px 0 0 0)`;
        visual.style.webkitClipPath = `inset(${localY}px 0 0 0)`;

        // Subtle parallax movement so the video/shapes physically move with scroll
        const innerContent = visual.firstElementChild;
        if (innerContent) {
          const parallax = (localY / visualHeight) * 100; // Translates down up to 100px while hidden
          innerContent.style.transform = `translateY(${parallax}px)`;
          
          // If it's a video, tie playback to scroll progress (scrubbing)
          if (innerContent.tagName && innerContent.tagName.toLowerCase() === 'video' && innerContent.duration) {
            const progress = 1 - (localY / visualHeight);
            // RequestAnimationFrame for smoother scrubbing
            requestAnimationFrame(() => {
              innerContent.currentTime = progress * innerContent.duration;
            });
          }
        }
      }
    }

    window.addEventListener('scroll', updateWipes, { passive: true });
    window.addEventListener('resize', updateWipes, { passive: true });
    
    // Run once on load to set initial state
    updateWipes();
  }

  // --- Dynamic Navbar Scroll Effect ---
  const navbars = document.querySelectorAll('.navbar-pill, .navbar-standard');
  if (navbars.length > 0) {
    window.addEventListener('scroll', () => {
      let threshold = 50; // default fallback
      
      // Determine the hero element to measure
      const heroElement = document.querySelector('.transition-wrapper') || document.querySelector('.hero-section') || document.querySelector('.hero');
      
      if (heroElement) {
        const rect = heroElement.getBoundingClientRect();
        const absoluteBottom = rect.bottom + window.scrollY;
        threshold = absoluteBottom - 80; // trigger slightly before fully passing
      }
      
      navbars.forEach(nav => {
        if (window.scrollY > threshold) {
          nav.classList.add('nav-scrolled');
        } else {
          nav.classList.remove('nav-scrolled');
        }
      });
    });
  }
  // --- Custom Blur Cursor for Multiple Sections ---
  const hoverCards = document.querySelectorAll('.grid-card, .industry-card, .insight-card, .new-work-item');
  if (hoverCards.length > 0) {
    const customCursor = document.createElement('div');
    customCursor.id = 'custom-blur-cursor';
    document.body.appendChild(customCursor);

    document.addEventListener('mousemove', (e) => {
      customCursor.style.left = e.clientX + 'px';
      customCursor.style.top = e.clientY + 'px';
    });

    hoverCards.forEach(card => {
      card.addEventListener('mouseenter', () => {
        if (card.classList.contains('industry-card')) {
          customCursor.textContent = 'Learn More';
        } else if (card.classList.contains('insight-card')) {
          customCursor.textContent = 'Read Insight';
        } else {
          customCursor.textContent = 'View Project';
        }
        customCursor.classList.add('active');
      });
      card.addEventListener('mouseleave', () => {
        customCursor.classList.remove('active');
      });
    });
  }

  // --- Full Screen Menu Logic ---
  const hamburgers = document.querySelectorAll('.hamburger');
  const fullScreenMenu = document.querySelector('.full-screen-menu');
  const menuClose = document.querySelector('.menu-close');

  if (fullScreenMenu && menuClose) {
    hamburgers.forEach(hamburger => {
      hamburger.addEventListener('click', () => {
        fullScreenMenu.classList.add('open');
        document.body.style.overflow = 'hidden'; // Lock scrolling
      });
    });

    menuClose.addEventListener('click', () => {
      fullScreenMenu.classList.remove('open');
      document.body.style.overflow = ''; // Restore scrolling
    });
  }

  // --- Text Scrub Animation on Scroll ---
  const scrubText = document.querySelector('.industries-intro');
  if (scrubText) {
    // Split text into words and wrap in spans
    const words = scrubText.innerText.split(' ');
    scrubText.innerHTML = '';
    words.forEach(word => {
      const span = document.createElement('span');
      span.innerText = word + ' ';
      span.style.opacity = '0.2'; // initial low opacity state
      span.style.transition = 'opacity 0.3s ease';
      scrubText.appendChild(span);
    });

    const spans = scrubText.querySelectorAll('span');

    window.addEventListener('scroll', () => {
      const rect = scrubText.getBoundingClientRect();
      const windowHeight = window.innerHeight;
      
      // The text starts revealing when it hits 80% down the screen,
      // and finishes revealing when it hits 40% down the screen.
      const startPoint = windowHeight * 0.8;
      const endPoint = windowHeight * 0.4;
      
      let progress = (startPoint - rect.top) / (startPoint - endPoint);
      progress = Math.max(0, Math.min(1, progress)); // Clamp between 0 and 1
      
      const wordsToReveal = Math.floor(progress * spans.length);
      
      spans.forEach((span, index) => {
        if (index < wordsToReveal) {
          span.style.opacity = '1';
        } else {
          span.style.opacity = '0.2';
        }
      });
    });
  }

  // --- Smooth Sticky Horizontal Scroll for Industries ---
  const industriesSection = document.getElementById('industries-scroll-section');
  const industriesTrack = document.getElementById('industries-track');
  const industriesProgressBar = document.getElementById('industries-progress-bar');
  
  if (industriesSection && industriesTrack) {
    let currentX = 0;
    let targetX = 0;
    let currentProgress = 0;
    let targetProgress = 0;
    
    window.addEventListener('scroll', () => {
      const rect = industriesSection.getBoundingClientRect();
      const windowHeight = window.innerHeight;
      
      // Calculate how far we've scrolled into the section.
      const scrollDistance = rect.height - windowHeight;
      
      // progress is 0 when rect.top == 0. progress is 1 when rect.top == -scrollDistance
      let progress = -rect.top / scrollDistance;
      progress = Math.max(0, Math.min(progress, 1));
      targetProgress = progress;
      
      // Calculate max translation required
      const maxTranslate = industriesTrack.scrollWidth - window.innerWidth + (window.innerWidth * 0.1);
      
      // If the content is wider than the screen, set target translation
      if (maxTranslate > 0) {
        if (rect.top <= 0) {
          targetX = -(progress * maxTranslate);
        } else {
          targetX = 0;
        }
      }
    }, { passive: true });
    
    // Use requestAnimationFrame for buttery smooth lerping (momentum)
    function renderScroll() {
      // Lerp: move currentX 8% of the way to targetX each frame
      currentX += (targetX - currentX) * 0.08;
      currentProgress += (targetProgress - currentProgress) * 0.08;
      
      // Avoid microscopic updates when almost there
      if (Math.abs(targetX - currentX) > 0.01) {
        industriesTrack.style.transform = `translateX(${currentX}px)`;
      }
      
      if (industriesProgressBar && Math.abs(targetProgress - currentProgress) > 0.001) {
        industriesProgressBar.style.transform = `scaleX(${currentProgress})`;
      }
      
      requestAnimationFrame(renderScroll);
    }
    
    renderScroll();
  }

  // ==========================================
  // EXPERTISE VERTICAL LINES SCROLL SCRUBBING
  // ==========================================
  const vLines = document.querySelectorAll('.expertise-v-line');
  const expertiseSection = document.getElementById('expertise-scroll-section');
  
  if (vLines.length > 0 && expertiseSection) {
    window.addEventListener('scroll', () => {
      const rect = expertiseSection.getBoundingClientRect();
      const windowHeight = window.innerHeight;
      
      let progress = 0;
      if (rect.top <= 0) {
        progress = -rect.top / (rect.height - windowHeight);
      }
      
      // Clamp between 0 and 1
      progress = Math.max(0, Math.min(progress, 1));
      
      // Apply to all vertical lines
      vLines.forEach(line => {
        line.style.transform = `scaleY(${progress})`;
      });

      // Apply staggered parallax to columns
      const pCols = document.querySelectorAll('.parallax-col');
      pCols.forEach(col => {
        const index = parseInt(col.getAttribute('data-index'));
        // E.g., index 0 stays at 0. index 4 drops by 200px when entering, moving up to 0.
        const maxOffset = index * 50; 
        const currentOffset = (1 - progress) * maxOffset;
        // Keep the content slightly faded until it reaches its final position
        const opacity = 0.5 + (0.5 * progress);
        
        col.style.transform = `translateY(${currentOffset}px)`;
        col.style.opacity = opacity;
      });

      // Apply to bottom horizontal line
      const hLine = document.querySelector('.expertise-h-line');
      if (hLine) {
        hLine.style.transform = `scaleX(${progress})`;
      }
    }, { passive: true });
  }

  // ==========================================
  // WATCH GIF IMAGE SEQUENCE (SCROLL SCRUBBING)
  // ==========================================
  const watchCanvas = document.getElementById('watch-canvas');
  const growthBlock = document.querySelector('.pathway-content-block[data-visual="visual-growth"]');
  
  if (watchCanvas && growthBlock) {
    const context = watchCanvas.getContext('2d');
    const frameCount = 240;
    const images = [];
    const imageLoaded = new Array(frameCount).fill(false);
    let firstFrameLoaded = false;
    let currentFrame = 79; // Start at frame 80
    let targetFrame = 79;

    // Helper to draw image like CSS 'object-fit: cover'
    function drawImageProp(ctx, img) {
      const w = ctx.canvas.width;
      const h = ctx.canvas.height;
      const iw = img.width;
      const ih = img.height;
      const r = Math.max(w / iw, h / ih);
      const nw = iw * r;
      const nh = ih * r;
      const cx = (w - nw) / 2;
      const cy = (h - nh) / 2;
      ctx.clearRect(0, 0, w, h);
      ctx.drawImage(img, cx, cy, nw, nh);
    }

    function resizeCanvas() {
      // Use parent container size
      const parent = watchCanvas.parentElement;
      const dpr = window.devicePixelRatio || 1;
      watchCanvas.width = parent.clientWidth * dpr;
      watchCanvas.height = parent.clientHeight * dpr;
      renderCurrentFrame();
    }
    window.addEventListener('resize', resizeCanvas);
    
    // Preload images
    for (let i = 1; i <= frameCount; i++) {
      const img = new Image();
      const paddedIndex = i.toString().padStart(3, '0');
      img.src = `ezgif-7757ef814a69e15f-jpg/ezgif-frame-${paddedIndex}.jpg`;
      img.onload = () => {
        imageLoaded[i - 1] = true;
        if (i === 1) {
          firstFrameLoaded = true;
          resizeCanvas(); // Set initial size and render
        }
      };
      images.push(img);
    }

    window.addEventListener('scroll', () => {
      const rect = growthBlock.getBoundingClientRect();
      const windowHeight = window.innerHeight;
      
      // Calculate progress: 0 when block enters from bottom, 1 when it leaves top
      const scrollDistance = windowHeight + rect.height;
      let progress = (windowHeight - rect.top) / scrollDistance;
      
      // Clamp progress
      progress = Math.max(0, Math.min(progress, 1));
      
      // We want to scrub from frame 80 to the end over this distance
      const startFrame = 79;
      targetFrame = startFrame + progress * (frameCount - 1 - startFrame);
    }, { passive: true });

    function renderCurrentFrame() {
      if (!firstFrameLoaded) return;
      
      const index = Math.round(currentFrame);
      const safeIndex = Math.max(0, Math.min(index, frameCount - 1));
      
      if (imageLoaded[safeIndex]) {
        drawImageProp(context, images[safeIndex]);
      } else {
        // Fallback to closest loaded
        for (let i = safeIndex; i >= 0; i--) {
          if (imageLoaded[i]) {
            drawImageProp(context, images[i]);
            break;
          }
        }
      }
    }

    function render() {
      currentFrame += (targetFrame - currentFrame) * 0.1; // Smooth momentum
      // Only render if we are moving significantly to save CPU
      if (Math.abs(targetFrame - currentFrame) > 0.01) {
        renderCurrentFrame();
      }
      requestAnimationFrame(render);
    }
    
    // Initial size setup
    setTimeout(resizeCanvas, 100);
    render();
  }

  // ==========================================
  // ROLLS ROYCE IMAGE SEQUENCE (SCROLL SCRUBBING)
  // ==========================================
  const rrCanvas = document.getElementById('rr-canvas');
  const expansionBlock = document.querySelector('.pathway-content-block[data-visual="visual-expansion"]');
  
  if (rrCanvas && expansionBlock) {
    const context = rrCanvas.getContext('2d');
    const frameCount = 90;
    const images = [];
    const imageLoaded = new Array(frameCount).fill(false);
    let firstFrameLoaded = false;
    let currentFrame = 0;
    let targetFrame = 0;

    function drawImagePropLocal(ctx, img) {
      const w = ctx.canvas.width;
      const h = ctx.canvas.height;
      const iw = img.width;
      const ih = img.height;
      const r = Math.max(w / iw, h / ih);
      const nw = iw * r;
      const nh = ih * r;
      const cx = (w - nw) / 2;
      // Shift video up by aligning to the bottom (1.0) instead of center (0.5)
      const verticalOffset = 1.0; 
      const cy = (h - nh) * verticalOffset;
      ctx.clearRect(0, 0, w, h);
      ctx.drawImage(img, cx, cy, nw, nh);
    }

    function resizeCanvasRR() {
      const parent = rrCanvas.parentElement;
      const dpr = window.devicePixelRatio || 1;
      rrCanvas.width = parent.clientWidth * dpr;
      rrCanvas.height = parent.clientHeight * dpr;
      renderCurrentFrameRR();
    }
    window.addEventListener('resize', resizeCanvasRR);
    
    for (let i = 1; i <= frameCount; i++) {
      const img = new Image();
      const paddedIndex = i.toString().padStart(3, '0');
      img.src = `about/ezgif-8fe79e3509e41e13-jpg/ezgif-frame-${paddedIndex}.jpg`;
      img.onload = () => {
        imageLoaded[i - 1] = true;
        if (i === 1) {
          firstFrameLoaded = true;
          resizeCanvasRR();
        }
      };
      images.push(img);
    }

    window.addEventListener('scroll', () => {
      const rect = expansionBlock.getBoundingClientRect();
      const windowHeight = window.innerHeight;
      
      const scrollDistance = windowHeight + rect.height;
      let progress = (windowHeight - rect.top) / scrollDistance;
      progress = Math.max(0, Math.min(progress, 1));
      
      targetFrame = progress * (frameCount - 1);
    }, { passive: true });

    function renderCurrentFrameRR() {
      if (!firstFrameLoaded) return;
      
      const index = Math.round(currentFrame);
      const safeIndex = Math.max(0, Math.min(index, frameCount - 1));
      
      if (imageLoaded[safeIndex]) {
        drawImagePropLocal(context, images[safeIndex]);
      } else {
        for (let i = safeIndex; i >= 0; i--) {
          if (imageLoaded[i]) {
            drawImagePropLocal(context, images[i]);
            break;
          }
        }
      }
    }

    function renderRR() {
      currentFrame += (targetFrame - currentFrame) * 0.1;
      if (Math.abs(targetFrame - currentFrame) > 0.01) {
        renderCurrentFrameRR();
      }
      requestAnimationFrame(renderRR);
    }
    
    setTimeout(resizeCanvasRR, 100);
    renderRR();
  }

  // ==========================================
  // MARKETING IMAGE SEQUENCE (SCROLL SCRUBBING)
  // ==========================================
  const marketingCanvas = document.getElementById('marketing-canvas');
  const marketingBlock = document.querySelector('.pathway-content-block[data-visual="visual-modernization"]');
  
  if (marketingCanvas && marketingBlock) {
    const context = marketingCanvas.getContext('2d');
    const frameCount = 90;
    const images = [];
    const imageLoaded = new Array(frameCount).fill(false);
    let firstFrameLoaded = false;
    let currentFrame = 0;
    let targetFrame = 0;

    function drawImagePropLocalMarketing(ctx, img) {
      const w = ctx.canvas.width;
      const h = ctx.canvas.height;
      const iw = img.width;
      const ih = img.height;
      const r = Math.max(w / iw, h / ih);
      const nw = iw * r;
      const nh = ih * r;
      const cx = (w - nw) / 2;
      const cy = (h - nh) / 2;
      ctx.clearRect(0, 0, w, h);
      ctx.drawImage(img, cx, cy, nw, nh);
    }

    function resizeCanvasMarketing() {
      const parent = marketingCanvas.parentElement;
      const dpr = window.devicePixelRatio || 1;
      marketingCanvas.width = parent.clientWidth * dpr;
      marketingCanvas.height = parent.clientHeight * dpr;
      renderCurrentFrameMarketing();
    }
    window.addEventListener('resize', resizeCanvasMarketing);
    
    for (let i = 1; i <= frameCount; i++) {
      const img = new Image();
      const paddedIndex = i.toString().padStart(3, '0');
      img.src = `about/WATCH/ezgif-frame-${paddedIndex}.jpg`;
      img.onload = () => {
        imageLoaded[i - 1] = true;
        if (i === 1) {
          firstFrameLoaded = true;
          resizeCanvasMarketing();
        }
      };
      images.push(img);
    }

    window.addEventListener('scroll', () => {
      const rect = marketingBlock.getBoundingClientRect();
      const windowHeight = window.innerHeight;
      
      const scrollDistance = windowHeight + rect.height;
      let progress = (windowHeight - rect.top) / scrollDistance;
      progress = Math.max(0, Math.min(progress, 1));
      
      targetFrame = progress * (frameCount - 1);
    }, { passive: true });

    function renderCurrentFrameMarketing() {
      if (!firstFrameLoaded) return;
      
      const index = Math.round(currentFrame);
      const safeIndex = Math.max(0, Math.min(index, frameCount - 1));
      
      if (imageLoaded[safeIndex]) {
        drawImagePropLocalMarketing(context, images[safeIndex]);
      } else {
        for (let i = safeIndex; i >= 0; i--) {
          if (imageLoaded[i]) {
            drawImagePropLocalMarketing(context, images[i]);
            break;
          }
        }
      }
    }

    function renderMarketing() {
      currentFrame += (targetFrame - currentFrame) * 0.1;
      if (Math.abs(targetFrame - currentFrame) > 0.01) {
        renderCurrentFrameMarketing();
      }
      requestAnimationFrame(renderMarketing);
    }
    
    setTimeout(resizeCanvasMarketing, 100);
    renderMarketing();
  }

  // ==========================================
  // WEBSITE DESIGN IMAGE SEQUENCE (SCROLL SCRUBBING)
  // ==========================================
  const wdCanvas = document.getElementById('web-design-canvas');
  const wdBlock = document.querySelector('.pathway-content-block[data-visual="visual-web-design"]');
  
  if (wdCanvas && wdBlock) {
    const context = wdCanvas.getContext('2d');
    const frameCount = 60;
    const images = [];
    const imageLoaded = new Array(frameCount).fill(false);
    let firstFrameLoaded = false;
    let currentFrame = 0;
    let targetFrame = 0;

    function drawImagePropLocalWD(ctx, img) {
      const w = ctx.canvas.width;
      const h = ctx.canvas.height;
      const iw = img.width;
      const ih = img.height;
      const r = Math.max(w / iw, h / ih);
      const nw = iw * r;
      const nh = ih * r;
      const cx = (w - nw) / 2;
      const verticalOffset = 0.5; // center
      const cy = (h - nh) * verticalOffset;
      ctx.clearRect(0, 0, w, h);
      ctx.drawImage(img, cx, cy, nw, nh);
    }

    function resizeCanvasWD() {
      const parent = wdCanvas.parentElement;
      const dpr = window.devicePixelRatio || 1;
      wdCanvas.width = parent.clientWidth * dpr;
      wdCanvas.height = parent.clientHeight * dpr;
      renderCurrentFrameWD();
    }
    window.addEventListener('resize', resizeCanvasWD);
    
    for (let i = 1; i <= frameCount; i++) {
      const img = new Image();
      const paddedIndex = i.toString().padStart(3, '0');
      img.src = `about/WEBSITE DESIGN/ezgif-frame-${paddedIndex}.jpg`;
      img.onload = () => {
        imageLoaded[i - 1] = true;
        if (i === 1) {
          firstFrameLoaded = true;
          resizeCanvasWD();
        }
      };
      images.push(img);
    }

    window.addEventListener('scroll', () => {
      const rect = wdBlock.getBoundingClientRect();
      const windowHeight = window.innerHeight;
      
      const scrollDistance = windowHeight + rect.height;
      let progress = (windowHeight - rect.top) / scrollDistance;
      progress = Math.max(0, Math.min(progress, 1));
      
      targetFrame = progress * (frameCount - 1);
    }, { passive: true });

    function renderCurrentFrameWD() {
      if (!firstFrameLoaded) return;
      
      const index = Math.round(currentFrame);
      const safeIndex = Math.max(0, Math.min(index, frameCount - 1));
      
      if (imageLoaded[safeIndex]) {
        drawImagePropLocalWD(context, images[safeIndex]);
      } else {
        for (let i = safeIndex; i >= 0; i--) {
          if (imageLoaded[i]) {
            drawImagePropLocalWD(context, images[i]);
            break;
          }
        }
      }
    }

    function renderWD() {
      currentFrame += (targetFrame - currentFrame) * 0.1;
      if (Math.abs(targetFrame - currentFrame) > 0.01) {
        renderCurrentFrameWD();
      }
      requestAnimationFrame(renderWD);
    }
    
    setTimeout(resizeCanvasWD, 100);
    renderWD();
  }

  // ==========================================
  // NORDEX FOCAL ROW ANIMATION
  // ==========================================
  const teamSection = document.getElementById('team-section');
  const cardLeft = document.getElementById('card-left');
  const cardCenter = document.getElementById('card-center');
  const cardRight = document.getElementById('card-right');

  if (teamSection && cardLeft && cardCenter && cardRight) {
    let currentProgress = 0;
    let targetProgress = 0;

    window.addEventListener('scroll', () => {
      const rect = teamSection.getBoundingClientRect();
      const scrollDistance = rect.height - window.innerHeight;
      
      // Calculate scroll progress from 0 to 1
      let progress = -rect.top / scrollDistance;
      progress = Math.max(0, Math.min(progress, 1));
      
      // Only animate on desktop, let CSS handle mobile
      if (window.innerWidth > 900) {
        targetProgress = progress;
      } else {
        targetProgress = 1;
      }
    }, { passive: true });

    function renderTeamRow() {
      // Smooth lerp
      currentProgress += (targetProgress - currentProgress) * 0.08;

      const textContainer = document.querySelector('.team-focal-viewport .container');

      if (window.innerWidth > 900) {
        if (textContainer) {
          textContainer.style.transform = `translateY(-${currentProgress * 80}px)`;
          textContainer.style.opacity = Math.max(0, 1 - currentProgress * 1.5);
        }

        // Modern Parallax Reveal (No gimmicky 3D or overlapping)
        // Center card moves up faster and fades in
        const centerTranslateY = (1 - currentProgress) * 20; // 20vh to 0vh
        const sideTranslateY = (1 - currentProgress) * 40; // 40vh to 0vh
        
        const opacity = Math.min(1, currentProgress * 2); // Fades in quickly

        cardCenter.style.transform = `translateY(${centerTranslateY}vh)`;
        cardCenter.style.opacity = opacity;

        cardLeft.style.transform = `translateY(${sideTranslateY}vh)`;
        cardLeft.style.opacity = opacity;
        
        cardRight.style.transform = `translateY(${sideTranslateY}vh)`;
        cardRight.style.opacity = opacity;
      } else {
        // Reset on mobile
        if (textContainer) {
          textContainer.style.transform = `none`;
          textContainer.style.opacity = 1;
        }
        cardCenter.style.transform = `none`;
        cardLeft.style.transform = `none`;
        cardLeft.style.opacity = 1;
        cardRight.style.transform = `none`;
        cardRight.style.opacity = 1;
      }

      requestAnimationFrame(renderTeamRow);
    }
    
    // Initial call to set target progress correctly
    window.dispatchEvent(new Event('scroll'));
    renderTeamRow();
  }

  // ==========================================
  // EXPERTISE MOBILE ACCORDION
  // ==========================================
  const expertiseCols = document.querySelectorAll('.expertise-col');
  expertiseCols.forEach(col => {
    col.addEventListener('click', () => {
      // Only toggle if we are in mobile view
      if (window.innerWidth <= 992) {
        col.classList.toggle('active');
      }
    });
  });

  // ==========================================
  // FOOTER MOBILE ACCORDION (GET IN TOUCH)
  // ==========================================
  const footerContact = document.querySelector('.footer-right .footer-label');
  if (footerContact) {
    footerContact.addEventListener('click', () => {
      if (window.innerWidth <= 992) {
        footerContact.parentElement.classList.toggle('active');
      }
    });
  }

});
