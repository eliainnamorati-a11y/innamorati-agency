document.addEventListener('DOMContentLoaded', () => {
  const canvas = document.getElementById('hero-canvas');
  if (!canvas) return;

  const context = canvas.getContext('2d');
  
  // Set up array for 150 frames
  const frameCount = 150;
  const images = [];
  
  // Object to track loading state
  const imageLoaded = new Array(frameCount).fill(false);
  let firstFrameLoaded = false;

  // Resize canvas to fill the screen
  function resizeCanvas() {
    const dpr = window.devicePixelRatio || 1;
    canvas.width = window.innerWidth * dpr;
    canvas.height = window.innerHeight * dpr;
    renderCurrentFrame();
  }
  window.addEventListener('resize', resizeCanvas);
  resizeCanvas();

  // Helper to draw image like CSS 'object-fit: cover'
  function drawImageProp(ctx, img) {
    const w = ctx.canvas.width;
    const h = ctx.canvas.height;
    const iw = img.width;
    const ih = img.height;
    
    // Calculate ratio to cover the canvas
    const r = Math.max(w / iw, h / ih);
    const nw = iw * r;
    const nh = ih * r;
    
    // Center it
    const cx = (w - nw) / 2;
    const cy = (h - nh) / 2;
    
    ctx.imageSmoothingEnabled = true;
    ctx.imageSmoothingQuality = 'high';
    
    ctx.clearRect(0, 0, w, h);
    ctx.drawImage(img, cx, cy, nw, nh);
  }

  // Preload images
  for (let i = 1; i <= frameCount; i++) {
    const img = new Image();
    // Zero-pad the index: 001 to 150
    const paddedIndex = i.toString().padStart(3, '0');
    img.src = `WATCH ANIMATION/ezgif-frame-${paddedIndex}.jpg`;
    
    img.onload = () => {
      imageLoaded[i - 1] = true;
      if (i === 1) {
        firstFrameLoaded = true;
        renderCurrentFrame();
      }
    };
    images.push(img);
  }

  // Scroll logic with Lerp (Momentum)
  const startFrame = 0;
  let currentFrame = startFrame;
  let targetFrame = startFrame;

  window.addEventListener('scroll', () => {
    const wrapper = document.querySelector('.transition-wrapper');
    if (!wrapper) return;
    
    // Get scroll progress through the wrapper
    const rect = wrapper.getBoundingClientRect();
    const scrollDistance = rect.height - window.innerHeight;
    
    // progress goes from 0 (at top) to 1 (at bottom of wrapper)
    let progress = -rect.top / scrollDistance;
    progress = Math.max(0, Math.min(progress, 1));
    
    // We want to start at frame 100
    targetFrame = startFrame + progress * (frameCount - 1 - startFrame);
  }, { passive: true });

  // Animation Loop
  function render() {
    // Lerp current frame towards target frame (smooth 8% momentum)
    currentFrame += (targetFrame - currentFrame) * 0.08;
    
    renderCurrentFrame();
    
    requestAnimationFrame(render);
  }

  function renderCurrentFrame() {
    if (!firstFrameLoaded) return;
    
    // Round to nearest integer to get the actual array index
    const index = Math.round(currentFrame);
    
    // Ensure we are within bounds
    const safeIndex = Math.max(0, Math.min(index, frameCount - 1));
    
    // Draw if loaded
    if (imageLoaded[safeIndex]) {
      drawImageProp(context, images[safeIndex]);
    } else {
      // Fallback to closest loaded frame if scrolling faster than loading
      for (let i = safeIndex; i >= 0; i--) {
        if (imageLoaded[i]) {
          drawImageProp(context, images[i]);
          break;
        }
      }
    }
  }

  // Start the loop
  render();
});
