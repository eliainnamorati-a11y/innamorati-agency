with open('melrose-kitchen.html', 'r') as f:
    html = f.read()

# Replace the missing closing divs for gallery-row
# The pattern is: two vertical images, then an empty line, then <!-- 1 Horizontal -->
# We need to insert a </div> before the <!-- 1 Horizontal --> if it's after a vertical row.

html = html.replace('object-fit: cover;"></div>\n      \n      <!-- 1 Horizontal -->', 'object-fit: cover;"></div>\n      </div>\n      \n      <!-- 1 Horizontal -->')
html = html.replace('object-fit: cover;"></div>\n\n      <!-- 1 Horizontal -->', 'object-fit: cover;"></div>\n      </div>\n\n      <!-- 1 Horizontal -->')

with open('melrose-kitchen.html', 'w') as f:
    f.write(html)
