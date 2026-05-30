import re

js_file = '/Users/eliainnamorati/Desktop/innamorati-agency-final/main.js'

with open(js_file, 'r') as f:
    content = f.read()

# We want to find `ctx.clearRect(0, 0, w, h);` and replace it with:
#       ctx.imageSmoothingEnabled = true;
#       ctx.imageSmoothingQuality = 'high';
#       ctx.clearRect(0, 0, w, h);

new_content = re.sub(r'(ctx\.clearRect\()', r'ctx.imageSmoothingEnabled = true;\n      ctx.imageSmoothingQuality = "high";\n      \1', content)

with open(js_file, 'w') as f:
    f.write(new_content)

print("Added image smoothing to main.js")
