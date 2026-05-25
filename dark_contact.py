with open("contact.html", "r") as f:
    text = f.read()

# 1. Body background
text = text.replace('<body style="background-color: var(--bg-light);">', '<body style="background-color: var(--bg-dark); color: white;">')

# 2. Navbar dark theme
text = text.replace('<nav class="navbar-pill light-theme">', '<nav class="navbar-pill dark-theme">')

# 3. Hero Section
text = text.replace('<section class="block-text-massive" style="padding-top: 15vw; padding-bottom: 4vw; background-color: var(--bg-light);">',
                    '<section class="block-text-massive" style="padding-top: 15vw; padding-bottom: 4vw; background-color: var(--bg-dark);">')
text = text.replace('<span class="label-muted">Contact</span>',
                    '<span class="label-muted" style="color: rgba(255,255,255,0.6);">Contact</span>')
text = text.replace('<h2 class="ambition-text blur-reveal-load" style="color:var(--text-dark);">Based in Geneva, <br><em>working worldwide.</em></h2>',
                    '<h2 class="ambition-text blur-reveal-load" style="color: white;">Based in Geneva, <br><em>working worldwide.</em></h2>')

# 4. Masonry Image Grid
text = text.replace('<section style="padding: 0 5vw 5vw; background-color: var(--bg-light);">',
                    '<section style="padding: 0 5vw 5vw; background-color: var(--bg-dark);">')

# 5. Contact Info Blocks Section
text = text.replace('<section style="padding: 5vw 5vw 15vw; background-color: var(--bg-light);">',
                    '<section style="padding: 5vw 5vw 15vw; background-color: var(--bg-dark);">')
text = text.replace('border-top: 1px solid rgba(0,0,0,0.1);', 'border-top: 1px solid rgba(255,255,255,0.1);')

# 6. Override the text colors for info-block
if '<style id="contact-dark-override">' not in text:
    style_override = """  <style id="contact-dark-override">
    .info-block p, .info-block a { color: white !important; }
    .info-block h4 { color: rgba(255,255,255,0.5) !important; opacity: 1 !important; }
  </style>
</head>"""
    text = text.replace('</head>', style_override)

with open("contact.html", "w") as f:
    f.write(text)
print("Updated contact.html to dark style.")
