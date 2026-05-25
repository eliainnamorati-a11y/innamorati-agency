import os
import re

new_footer_complex = """  <footer class="footer-complex">
    <div class="footer-main">
      <div class="footer-left">
        <div class="footer-grid-2">
          <div class="footer-col">
            <span class="footer-label">GENEVA STUDIO</span>
            <p>Geneva</p>
            <a href="contact.html" class="view-all-link footer-link-circle">Geneva Studio <span class="arrow-circle">&rarr;</span></a>
          </div>
          <div class="footer-col">
            <span class="footer-label">MIAMI STUDIO</span>
            <p>Miami</p>
            <a href="contact.html" class="view-all-link footer-link-circle">Miami Studio <span class="arrow-circle">&rarr;</span></a>
          </div>
          <div class="footer-col">
            <span class="footer-label">CONTACT</span>
            <p>elia@innamorati.ch<br>+41 79 309 0690</p>
            <a href="contact.html" class="view-all-link footer-link-circle" style="margin-top: 15px;">Start a Project <span class="arrow-circle">&rarr;</span></a>
          </div>
          <div class="footer-col">
            <span class="footer-label">CONNECT</span>
            <ul class="footer-socials">
              <li><a href="#">LinkedIn</a></li>
              <li><a href="#">Instagram</a></li>
              <li><a href="#">Behance</a></li>
            </ul>
          </div>
        </div>
      </div>

      <div class="footer-right">
        <span class="footer-label">GET IN TOUCH</span>
        <form class="footer-form">
          <div class="form-row">
            <input type="text" placeholder="Your Name*">
            <input type="email" placeholder="Your Email*">
          </div>
          <div class="form-row">
            <input type="text" placeholder="Phone Number">
            <input type="text" placeholder="Company Name">
          </div>
          <div class="form-row full-width">
            <input type="text" placeholder="Message*">
          </div>
          <div class="form-submit-row">
            <button type="submit" class="view-all-link submit-btn" style="background:transparent; border:none; padding:0; cursor:pointer;">Send Message <span class="arrow-circle">&rarr;</span></button>
          </div>
        </form>
      </div>
    </div>

    <div class="footer-bottom-bar">
      <div class="footer-bar-left">
        <a href="#">PRIVACY / COOKIES POLICY</a>
      </div>
      <div class="footer-bar-center">
        <a href="works.html">CASE STUDIES</a>
        <a href="about.html">ABOUT</a>
        <a href="insights.html">INSIGHTS</a>
        <a href="contact.html">CONTACT</a>
      </div>
      <div class="footer-bar-right">
        <span class="footer-brand">Innamorati.</span>
      </div>
    </div>

    <div class="footer-legal">
      <div class="legal-left">
        Innamorati Agency Limited.
      </div>
      <div class="legal-right">
        &copy; 2024 - 2026 Innamorati.
      </div>
    </div>
  </footer>"""

new_menu_footer = """  <div class="menu-footer">
    <div class="menu-footer-block">
      <span>Visit</span>
      <p>Geneva &amp; Miami</p>
    </div>
    <div class="menu-footer-block">
      <span>Work With Us</span>
      <a href="mailto:elia@innamorati.ch">elia@innamorati.ch</a>
      <a href="contact.html">Schedule a call</a>
    </div>
  </div>"""

directory = '/Users/eliainnamorati/Desktop/innamorati-agency-final'
html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

for f in html_files:
    path = os.path.join(directory, f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace the footer complex
    new_content = re.sub(r'<footer class="footer-complex">.*?</footer>', new_footer_complex, content, flags=re.DOTALL)
    
    # Replace the menu footer
    new_content = re.sub(r'<div class="menu-footer">.*?</div>\s*</div>\s*</body>', new_menu_footer + '\n</div>\n</body>', new_content, flags=re.DOTALL)
    
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated footer in {f}")
