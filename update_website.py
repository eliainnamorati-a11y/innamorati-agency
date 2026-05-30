import re

js_file = '/Users/eliainnamorati/Desktop/innamorati-agency-final/main.js'

with open(js_file, 'r') as f:
    content = f.read()

# We need to replace the watchCanvas block
# It starts with:
#   const watchCanvas = document.getElementById('watch-canvas');
# And ends with the end of that if-block.

watch_block_regex = re.compile(r'const watchCanvas = document\.getElementById\(\'watch-canvas\'\);.*?\}\n', re.DOTALL)

replacement = """const websiteCanvas = document.getElementById('website-canvas');
  const growthBlock = document.querySelector('.pathway-content-block[data-visual="visual-growth"]');
  
  if (websiteCanvas && growthBlock) {
    const context = websiteCanvas.getContext('2d');
    const frameCount = 120;
    const images = [];
    const imageLoaded = new Array(frameCount).fill(false);
    let firstFrameLoaded = false;
    let currentFrame = 0;
    let targetFrame = 0;

    function drawImagePropWebsite(ctx, img) {
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

    function resizeCanvasWebsite() {
      const parent = websiteCanvas.parentElement;
      const dpr = window.devicePixelRatio || 1;
      websiteCanvas.width = parent.clientWidth * dpr;
      websiteCanvas.height = parent.clientHeight * dpr;
      renderCurrentFrameWebsite();
    }
    window.addEventListener('resize', resizeCanvasWebsite);
    
    for (let i = 1; i <= frameCount; i++) {
      const img = new Image();
      const paddedIndex = i.toString().padStart(3, '0');
      img.src = `about/website/ezgif-frame-${paddedIndex}.jpg`;
      img.onload = () => {
        imageLoaded[i - 1] = true;
        if (i === 1) {
          firstFrameLoaded = true;
          resizeCanvasWebsite();
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

    function renderCurrentFrameWebsite() {
      if (!firstFrameLoaded) return;
      const index = Math.round(currentFrame);
      const safeIndex = Math.max(0, Math.min(index, frameCount - 1));
      if (imageLoaded[safeIndex]) drawImagePropWebsite(context, images[safeIndex]);
      else {
        for (let i = safeIndex; i >= 0; i--) {
          if (imageLoaded[i]) { drawImagePropWebsite(context, images[i]); break; }
        }
      }
    }

    function renderWebsite() {
      currentFrame += (targetFrame - currentFrame) * 0.1;
      if (Math.abs(targetFrame - currentFrame) > 0.01) {
        renderCurrentFrameWebsite();
      }
      requestAnimationFrame(renderWebsite);
    }
    renderWebsite();
  }
"""

if re.search(watch_block_regex, content):
    new_content = re.sub(watch_block_regex, replacement, content, count=1)
    with open(js_file, 'w') as f:
        f.write(new_content)
    print("Successfully replaced watchCanvas with websiteCanvas!")
else:
    print("Could not find watchCanvas block!")
