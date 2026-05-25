import re
with open('melrose-kitchen.html', 'r') as f:
    html = f.read()

# Replace <img class="reveal-up"...> with slide-reveal-mask wrappers
def replace_img(match):
    full_tag = match.group(0)
    # Extract src
    src_match = re.search(r'src="([^"]+)"', full_tag)
    src = src_match.group(1) if src_match else ''
    
    # Check if it's horizontal or vertical based on aspect-ratio or style
    if 'aspect-ratio: 16/9' in full_tag:
        return f'<div class="slide-reveal-mask" style="width: 100%; margin-top:2vw; border-radius:4px; aspect-ratio: 16/9;"><img src="{src}" style="width: 100%; height: 100%; object-fit: cover;"></div>'
    elif 'aspect-ratio: 4/5' in full_tag:
        return f'<div class="slide-reveal-mask" style="width: 100%; height: 100%; aspect-ratio: 4/5; border-radius:4px;"><img src="{src}" style="width: 100%; height: 100%; object-fit: cover;"></div>'
    return full_tag

# Only target the standalone images and vertical grid images
html = re.sub(r'<img [^>]+aspect-ratio[^>]+>', replace_img, html)

# Fix the first gallery-hero image which was inside a div
html = html.replace('<div class="gallery-hero reveal-up">\n        <div class="slide-reveal-mask"', '<div class="slide-reveal-mask"')
html = html.replace('object-fit: cover;"></div>\n      </div>', 'object-fit: cover;"></div>')

with open('melrose-kitchen.html', 'w') as f:
    f.write(html)
