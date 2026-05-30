import sys
import re

js_file = '/Users/eliainnamorati/Desktop/innamorati-agency-final/main.js'

with open(js_file, 'r') as f:
    content = f.read()

# We want to replace the WATCH GIF IMAGE SEQUENCE block with the naming-canvas block.
# Since I modified it with image smoothing, the regex needs to be more forgiving.
watch_regex = re.compile(r'// ==========================================\n\s*// WATCH GIF IMAGE SEQUENCE.*?setTimeout\(resizeCanvas, 100\);\n\s*\}\n?', re.DOTALL)

replacement = """// ==========================================
  // BRAND NAMING & MESSAGING IMAGE SEQUENCE (SCROLL SCRUBBING)
  // ==========================================
  const namingCanvas = document.getElementById('naming-canvas');
  const growthBlock = document.querySelector('.pathway-content-block[data-visual="visual-growth"]');
  
  if (namingCanvas && growthBlock) {
    const context = namingCanvas.getContext('2d');
    const frameCount = 120;
    const images = [];
    const imageLoaded = new Array(frameCount).fill(false);
    let firstFrameLoaded = false;
    let currentFrame = 0;
    let targetFrame = 0;

    function drawImagePropNaming(ctx, img) {
      const w = ctx.canvas.width;
      const h = ctx.canvas.height;
      const iw = img.width;
      const ih = img.height;
      const r = Math.max(w / iw, h / ih);
      const nw = iw * r;
      const nh = ih * r;
      const cx = (w - nw) / 2;
      const cy = (h - nh) / 2;
      ctx.imageSmoothingEnabled = true;
      ctx.imageSmoothingQuality = "high";
      ctx.clearRect(0, 0, w, h);
      ctx.drawImage(img, cx, cy, nw, nh);
    }

    function resizeCanvasNaming() {
      const parent = namingCanvas.parentElement;
      const dpr = window.devicePixelRatio || 1;
      namingCanvas.width = parent.clientWidth * dpr;
      namingCanvas.height = parent.clientHeight * dpr;
      renderCurrentFrameNaming();
    }
    window.addEventListener('resize', resizeCanvasNaming);
    
    for (let i = 1; i <= frameCount; i++) {
      const img = new Image();
      const paddedIndex = i.toString().padStart(3, '0');
      img.src = `about/website/ezgif-frame-${paddedIndex}.jpg`;
      img.onload = () => {
        imageLoaded[i - 1] = true;
        if (i === 1) {
          firstFrameLoaded = true;
          resizeCanvasNaming();
        }
      };
      images.push(img);
    }

    window.addEventListener('scroll', () => {
      const rect = growthBlock.getBoundingClientRect();
      const windowHeight = window.innerHeight;
      
      const scrollDistance = windowHeight + rect.height;
      let progress = (windowHeight - rect.top) / scrollDistance;
      progress = Math.max(0, Math.min(progress, 1));
      
      targetFrame = progress * (frameCount - 1);
    }, { passive: true });

    function renderCurrentFrameNaming() {
      if (!firstFrameLoaded) return;
      
      const index = Math.round(currentFrame);
      const safeIndex = Math.max(0, Math.min(index, frameCount - 1));
      
      if (imageLoaded[safeIndex]) {
        drawImagePropNaming(context, images[safeIndex]);
      } else {
        for (let i = safeIndex; i >= 0; i--) {
          if (imageLoaded[i]) {
            drawImagePropNaming(context, images[i]);
            break;
          }
        }
      }
    }

    function renderNaming() {
      currentFrame += (targetFrame - currentFrame) * 0.1;
      if (Math.abs(targetFrame - currentFrame) > 0.01) {
        renderCurrentFrameNaming();
      }
      requestAnimationFrame(renderNaming);
    }
    
    setTimeout(resizeCanvasNaming, 100);
    renderNaming();
  }
"""

if re.search(watch_regex, content):
    new_content = re.sub(watch_regex, replacement, content)
    with open(js_file, 'w') as f:
        f.write(new_content)
    print("Replaced watch-canvas with naming-canvas!")
else:
    print("Could not find regex pattern!")
