document.addEventListener('DOMContentLoaded', () => {
  /* ==========================================
     1. Hero Text Reveal (Staggered Animation)
     ========================================== */
  const revealTextEl = document.querySelector('.reveal-text');
  if (revealTextEl) {
    // Split text into words for staggered reveal
    const text = revealTextEl.innerText;
    const words = text.split(' ');
    revealTextEl.innerHTML = '';
    
    words.forEach((word, i) => {
      const span = document.createElement('span');
      span.innerText = word + ' ';
      span.style.transitionDelay = `${i * 0.05}s`;
      revealTextEl.appendChild(span);
    });

    // Use IntersectionObserver to trigger reveal when in view
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const spans = entry.target.querySelectorAll('span');
          spans.forEach(span => span.classList.add('revealed'));
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.2 });

    observer.observe(revealTextEl);
  }

  /* ==========================================
     2. Project List Hover Image Reveal
     ========================================== */
  const projectItems = document.querySelectorAll('.project-hover-list li');
  const imageRevealEl = document.querySelector('.hover-image-reveal');
  
  if (projectItems.length && imageRevealEl) {
    let mouseX = 0;
    let mouseY = 0;
    let targetX = 0;
    let targetY = 0;

    // Smooth follow cursor logic
    function animateImage() {
      // Lerp for smooth following
      mouseX += (targetX - mouseX) * 0.1;
      mouseY += (targetY - mouseY) * 0.1;
      
      imageRevealEl.style.left = `${mouseX}px`;
      imageRevealEl.style.top = `${mouseY}px`;
      
      requestAnimationFrame(animateImage);
    }
    animateImage();

    window.addEventListener('mousemove', (e) => {
      targetX = e.clientX;
      targetY = e.clientY;
    });

    projectItems.forEach(item => {
      item.addEventListener('mouseenter', () => {
        const bgImage = item.getAttribute('data-image');
        if (bgImage) {
          imageRevealEl.style.backgroundImage = `url(${bgImage})`;
        }
        imageRevealEl.classList.add('active');
      });

      item.addEventListener('mouseleave', () => {
        imageRevealEl.classList.remove('active');
      });
    });
  }

  /* ==========================================
     3. FAQ Accordion Logic
     ========================================== */
  const faqHeaders = document.querySelectorAll('.faq-header');
  
  faqHeaders.forEach(header => {
    header.addEventListener('click', () => {
      const faqItem = header.parentElement;
      const faqBody = faqItem.querySelector('.faq-body');
      
      // Close others
      document.querySelectorAll('.faq-item').forEach(item => {
        if (item !== faqItem) {
          item.classList.remove('active');
          item.querySelector('.faq-body').style.maxHeight = null;
        }
      });

      // Toggle current
      faqItem.classList.toggle('active');
      
      if (faqItem.classList.contains('active')) {
        faqBody.style.maxHeight = faqBody.scrollHeight + "px";
      } else {
        faqBody.style.maxHeight = null;
      }
    });
  });

  /* ==========================================
     4. Parallax Scrub on Scroll (Services Grid)
     ========================================== */
  const scrubElements = document.querySelectorAll('.scrub-scroll');
  
  if (scrubElements.length) {
    function onScroll() {
      const windowHeight = window.innerHeight;
      
      scrubElements.forEach(el => {
        // Use parent for bounding box so it doesn't shift
        const parent = el.parentElement;
        const rect = parent.getBoundingClientRect();
        
        // Calculate progress based on distance from bottom of viewport
        const triggerPoint = windowHeight * 0.8; // 80% of window height for the full scroll window
        let scrollFraction = (windowHeight - rect.top) / triggerPoint; 
        
        // Use the index of the element to stagger its start point "one by one"
        const index = Array.from(scrubElements).indexOf(el);
        const staggerOffset = index * 0.15; // 0.15 fraction delay per column
        
        let rawProgress = scrollFraction - staggerOffset;
        
        // Multiply by 3.0 so each column completes its animation quickly once it starts
        // Clamp between 0 and 1
        let progress = Math.max(0, Math.min(rawProgress * 3.0, 1));
        
        // All columns translate exactly the same distance, but at different times
        const maxOffset = 300; // Start 300px down
        const currentTranslate = maxOffset * (1 - progress);
        
        // Apply transform and opacity
        el.style.transform = `translateY(${currentTranslate}px)`;
        el.style.opacity = progress;
      });
    }
    
    window.addEventListener('scroll', onScroll, { passive: true });
    // Trigger once on load
    onScroll();
  }

  /* ==========================================
     5. Divider Progress Lines
     ========================================== */
  const scrollLines = document.querySelectorAll('.scrub-scroll-line');
  if (scrollLines.length) {
    function onScrollLines() {
      const windowHeight = window.innerHeight;
      scrollLines.forEach(line => {
        const parent = line.parentElement;
        const rect = parent.getBoundingClientRect();
        
        // Progress goes from 0 to 1 as the line moves from the bottom to the middle of the screen
        const triggerPoint = windowHeight * 0.5;
        let rawProgress = (windowHeight - rect.top) / triggerPoint;
        let progress = Math.max(0, Math.min(rawProgress, 1));
        
        line.style.width = `${progress * 100}%`;
      });
    }
    window.addEventListener('scroll', onScrollLines, { passive: true });
    onScrollLines();
  }
});
