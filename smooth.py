import re

with open('main.js', 'r') as f:
    content = f.read()

def replace_draw_image(match):
    name = match.group(1)
    return f'''    function drawImageProp{name}(ctx, img, alpha = 1.0) {{
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
      ctx.globalAlpha = alpha;
      if (alpha === 1.0) ctx.clearRect(0, 0, w, h);
      ctx.drawImage(img, cx, cy, nw, nh);
      ctx.globalAlpha = 1.0;
    }}'''

content = re.sub(
    r'    function drawImageProp(\w+)\(ctx, img\) \{\s*const w = ctx\.canvas\.width;[\s\S]*?ctx\.drawImage\(img, cx, cy, nw, nh\);\s*\}',
    replace_draw_image,
    content
)

def replace_render_frame(match):
    name = match.group(1)
    return f'''    function renderCurrentFrame{name}() {{
      if (!firstFrameLoaded) return;
      
      const index1 = Math.floor(currentFrame);
      const index2 = Math.min(index1 + 1, frameCount - 1);
      const alpha = currentFrame - index1;
      
      const safeIndex1 = Math.max(0, Math.min(index1, frameCount - 1));
      const safeIndex2 = Math.max(0, Math.min(index2, frameCount - 1));
      
      let drawImg1 = null;
      if (imageLoaded[safeIndex1]) drawImg1 = images[safeIndex1];
      else {{
        for (let i = safeIndex1; i >= 0; i--) {{
          if (imageLoaded[i]) {{ drawImg1 = images[i]; break; }}
        }}
      }}
      
      if (drawImg1) drawImageProp{name}(context, drawImg1, 1.0);
      
      if (alpha > 0.01 && safeIndex1 !== safeIndex2 && imageLoaded[safeIndex2]) {{
        drawImageProp{name}(context, images[safeIndex2], alpha);
      }}
    }}'''

content = re.sub(
    r'    function renderCurrentFrame(\w+)\(\) \{\s*if \(\!firstFrameLoaded\) return;\s*const index = Math\.round\(currentFrame\);[\s\S]*?\}\s*\}',
    replace_render_frame,
    content
)

# Smooth lerp from 0.1 to 0.06 for better physics
content = re.sub(r'currentFrame \+= \(targetFrame - currentFrame\) \* 0\.1;', r'currentFrame += (targetFrame - currentFrame) * 0.06;', content)

with open('main.js', 'w') as f:
    f.write(content)

print("Done")
