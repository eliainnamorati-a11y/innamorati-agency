import os
import re

nav_replacement = """  <nav class="navbar-pill light-theme">
    <div class="logo"><a href="index.html">Innamorati</a></div>
    <ul class="nav-links">
      <li><a href="works.html">Case Studies</a></li>
      <li><a href="about.html">About</a></li>
      <li><a href="insights.html">Insights</a></li>
      <li><a href="contact.html">Contact</a></li>
    </ul>
    <div class="hamburger"><span></span><span></span></div>
  </nav>"""

directory = "/Users/eliainnamorati/Desktop/innamorati-agency-final"
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Replace everything from <nav to </nav>
        new_content = re.sub(r'<nav[^>]*>.*?</nav>', nav_replacement, content, flags=re.DOTALL)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")

