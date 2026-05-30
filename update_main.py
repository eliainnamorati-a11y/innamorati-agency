import sys

js_file = '/Users/eliainnamorati/Desktop/innamorati-agency-final/main.js'

with open(js_file, 'r') as f:
    content = f.read()

import re

# Find the rrCanvas block to replace
rr_block_regex = re.compile(r'// ==========================================\n\s*// ROLLS ROYCE IMAGE SEQUENCE.*?renderRR\(\);\n\s*}', re.DOTALL)

replacement = """// ==========================================
  // BRAND DESIGN IMAGE SEQUENCE (SCROLL SCRUBBING)
  // ==========================================
  const designCanvas = document.getElementById('design-canvas');
  const expansionBlock = document.querySelector('.pathway-content-block[data-visual="visual-expansion"]');
  
  if (designCanvas && expansionBlock) {
    const context = designCanvas.getContext('2d');
    const frameCount = 90;
    const images = [];
    const imageLoaded = new Array(frameCount).fill(false);
    let firstFrameLoaded = false;
    let currentFrame = 0;
    let targetFrame = 0;

    function drawImagePropDesign(ctx, img) {
      const w = ctx.canvas.width;
      const h = ctx.canvas.height;
      const iw = img.width;
      const ih = img.height;
      const r = Math.max(w / iw, h / ih);
      const nw = iw * r;
      const nh = ih * r;
      const cx = (w - nw) / 2;
      const cy = (h - nh) / 2; // centered
      ctx.clearRect(0, 0, w, h);
      ctx.drawImage(img, cx, cy, nw, nh);
    }

    function resizeCanvasDesign() {
      const parent = designCanvas.parentElement;
      const dpr = window.devicePixelRatio || 1;
      designCanvas.width = parent.clientWidth * dpr;
      designCanvas.height = parent.clientHeight * dpr;
      renderCurrentFrameDesign();
    }
    window.addEventListener('resize', resizeCanvasDesign);
    
    for (let i = 1; i <= frameCount; i++) {
      const img = new Image();
      const paddedIndex = i.toString().padStart(3, '0');
      img.src = `about/chart/ezgif-frame-${paddedIndex}.jpg`;
      img.onload = () => {
        imageLoaded[i - 1] = true;
        if (i === 1) {
          firstFrameLoaded = true;
          resizeCanvasDesign();
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

    function renderCurrentFrameDesign() {
      if (!firstFrameLoaded) return;
      const index = Math.round(currentFrame);
      const safeIndex = Math.max(0, Math.min(index, frameCount - 1));
      if (imageLoaded[safeIndex]) drawImagePropDesign(context, images[safeIndex]);
      else {
        for (let i = safeIndex; i >= 0; i--) {
          if (imageLoaded[i]) { drawImagePropDesign(context, images[i]); break; }
        }
      }
    }

    function renderDesign() {
      currentFrame += (targetFrame - currentFrame) * 0.1;
      if (Math.abs(targetFrame - currentFrame) > 0.01) {
        renderCurrentFrameDesign();
      }
      requestAnimationFrame(renderDesign);
    }
    renderDesign();
  }

  // ==========================================
  // BRAND STRATEGY IMAGE SEQUENCE (SCROLL SCRUBBING)
  // ==========================================
  const strategyCanvas = document.getElementById('strategy-canvas');
  const creationBlock = document.querySelector('.pathway-content-block[data-visual="visual-creation"]');
  
  if (strategyCanvas && creationBlock) {
    const context = strategyCanvas.getContext('2d');
    const frameCount = 60;
    const images = [];
    const imageLoaded = new Array(frameCount).fill(false);
    let firstFrameLoaded = false;
    let currentFrame = 0;
    let targetFrame = 0;

    function drawImagePropStrategy(ctx, img) {
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

    function resizeCanvasStrategy() {
      const parent = strategyCanvas.parentElement;
      const dpr = window.devicePixelRatio || 1;
      strategyCanvas.width = parent.clientWidth * dpr;
      strategyCanvas.height = parent.clientHeight * dpr;
      renderCurrentFrameStrategy();
    }
    window.addEventListener('resize', resizeCanvasStrategy);
    
    for (let i = 1; i <= frameCount; i++) {
      const img = new Image();
      const paddedIndex = i.toString().padStart(3, '0');
      img.src = `about/logo/ezgif-frame-${paddedIndex}.jpg`;
      img.onload = () => {
        imageLoaded[i - 1] = true;
        if (i === 1) {
          firstFrameLoaded = true;
          resizeCanvasStrategy();
        }
      };
      images.push(img);
    }

    window.addEventListener('scroll', () => {
      const rect = creationBlock.getBoundingClientRect();
      const windowHeight = window.innerHeight;
      
      const scrollDistance = windowHeight + rect.height;
      let progress = (windowHeight - rect.top) / scrollDistance;
      progress = Math.max(0, Math.min(progress, 1));
      
      targetFrame = progress * (frameCount - 1);
    }, { passive: true });

    function renderCurrentFrameStrategy() {
      if (!firstFrameLoaded) return;
      const index = Math.round(currentFrame);
      const safeIndex = Math.max(0, Math.min(index, frameCount - 1));
      if (imageLoaded[safeIndex]) drawImagePropStrategy(context, images[safeIndex]);
      else {
        for (let i = safeIndex; i >= 0; i--) {
          if (imageLoaded[i]) { drawImagePropStrategy(context, images[i]); break; }
        }
      }
    }

    function renderStrategy() {
      currentFrame += (targetFrame - currentFrame) * 0.1;
      if (Math.abs(targetFrame - currentFrame) > 0.01) {
        renderCurrentFrameStrategy();
      }
      requestAnimationFrame(renderStrategy);
    }
    renderStrategy();
  }"""

if re.search(rr_block_regex, content):
    new_content = re.sub(rr_block_regex, replacement, content)
    with open(js_file, 'w') as f:
        f.write(new_content)
    print("Successfully replaced main.js!")
else:
    print("Could not find regex pattern!")
