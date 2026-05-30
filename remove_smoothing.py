import re

js_file = '/Users/eliainnamorati/Desktop/innamorati-agency-final/main.js'

with open(js_file, 'r') as f:
    content = f.read()

# Remove the two imageSmoothing lines
new_content = re.sub(r'\s*ctx\.imageSmoothingEnabled = true;\n\s*ctx\.imageSmoothingQuality = "high";\n', '\n', content)

with open(js_file, 'w') as f:
    f.write(new_content)

print("Removed image smoothing")
