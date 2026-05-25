import os
import re

directory = "/Users/eliainnamorati/Desktop/innamorati-agency-final"

nav_old = """      <li><a href="works.html">Case Studies</a></li>
      <li><a href="about.html">About</a></li>
      <li><a href="insights.html">Insights</a></li>
      <li><a href="contact.html">Contact</a></li>"""

nav_new = """      <li><a href="works.html">Case Studies</a></li>
      <li><a href="services.html">Services</a></li>
      <li><a href="studio.html">Our Studio</a></li>
      <li><a href="insights.html">Insights</a></li>
      <li><a href="contact.html">Contact</a></li>"""

footer_old = """        <a href="works.html">CASE STUDIES</a>
        <a href="about.html">ABOUT</a>
        <a href="insights.html">INSIGHTS</a>
        <a href="contact.html">CONTACT</a>"""

footer_new = """        <a href="works.html">CASE STUDIES</a>
        <a href="services.html">SERVICES</a>
        <a href="studio.html">OUR STUDIO</a>
        <a href="insights.html">INSIGHTS</a>
        <a href="contact.html">CONTACT</a>"""

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace(nav_old, nav_new)
        content = content.replace(footer_old, footer_new)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Processed {filename}")
