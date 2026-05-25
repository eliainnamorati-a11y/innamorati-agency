import os

directory = "/Users/eliainnamorati/Desktop/innamorati-agency-final"

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Fix navigation text from Our Studio -> Studio
        content = content.replace('<li><a href="studio.html">Our Studio</a></li>', '<li><a href="studio.html">Studio</a></li>')
        content = content.replace('<a href="studio.html">OUR STUDIO</a>', '<a href="studio.html">STUDIO</a>')
        
        # Fix the fullscreen menu if it still has "Approach"
        old_menu = """      <li><a href="about.html">Approach</a></li>"""
        new_menu = """      <li><a href="services.html">Services</a></li>\n      <li><a href="studio.html">Studio</a></li>"""
        content = content.replace(old_menu, new_menu)
        
        # In studio.html specifically, fix the title and header if they say "Our Studio"
        if filename == "studio.html":
            content = content.replace("<title>Our Studio | Innamorati Agency</title>", "<title>Studio | Innamorati Agency</title>")
            # If the hero section still says "We defy convention to accelerate business." or "Our Studio"
            content = content.replace("Our Studio", "Studio")

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Processed {filename}")
