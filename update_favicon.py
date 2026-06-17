import os
import glob

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r') as f:
        content = f.read()
    
    # Replace the existing icon or add it if it doesn't exist
    if '<link rel="icon"' in content:
        import re
        content = re.sub(r'<link rel="icon"[^>]*>', '<link rel="icon" type="image/png" href="icon%20for%20web.png">', content)
    else:
        # If not present, insert it before </head>
        content = content.replace('</head>', '  <link rel="icon" type="image/png" href="icon%20for%20web.png">\n</head>')
        
    with open(file, 'w') as f:
        f.write(content)

print(f"Updated favicon in {len(html_files)} HTML files.")
