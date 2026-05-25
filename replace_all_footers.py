import os
import re

complex_footer = """  <footer class="footer-complex">
    <div class="footer-main">
      <div class="footer-left">
        <div class="footer-grid-2">
          <div class="footer-col">
            <span class="footer-label">THE STUDIO</span>
            <p>New York Studio,<br>123 Broadway,<br>New York, NY 10001</p>
            <a href="contact.html" class="view-all-link footer-link-circle">New York Studio <span class="arrow-circle">&rarr;</span></a>
          </div>
          <div class="footer-col">
            <span class="footer-label">SWISS OFFICE</span>
            <p>Zurich Office,<br>Bahnhofstrasse 1,<br>8001 Zurich</p>
            <a href="contact.html" class="view-all-link footer-link-circle">Zurich Office <span class="arrow-circle">&rarr;</span></a>
          </div>
          <div class="footer-col">
            <span class="footer-label">CONTACT</span>
            <p>elia@innamorati.ch<br>+1 202 555 0123</p>
            <a href="contact.html" class="view-all-link footer-link-circle" style="margin-top: 15px;">Start a Project <span class="arrow-circle">&rarr;</span></a>
          </div>
          <div class="footer-col">
            <span class="footer-label">CONNECT</span>
            <ul class="footer-socials">
              <li><a href="#">LinkedIn</a></li>
              <li><a href="#">Instagram</a></li>
              <li><a href="#">Dribbble</a></li>
              <li><a href="#">Behance</a></li>
              <li><a href="#">Pinterest</a></li>
              <li><a href="#">Facebook</a></li>
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
        <a href="works.html">WORK</a>
        <a href="about.html">SERVICES</a>
        <a href="insights.html">STUDIO</a>
        <a href="insights.html">MUSE</a>
        <a href="contact.html">CONTACT</a>
      </div>
      <div class="footer-bar-right">
        <span class="footer-brand">Innamorati.</span>
      </div>
    </div>

    <div class="footer-legal">
      <div class="legal-left">
        Innamorati Agency Limited. VAT Reg No. GB 123 4567 89 Company Reg No. 12345678 Registered Address: New York, USA
      </div>
      <div class="legal-right">
        &copy; 2015 - 2026 Innamorati.
      </div>
    </div>
  </footer>"""

directory = '/Users/eliainnamorati/Desktop/innamorati-agency-final'
html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

for f in html_files:
    path = os.path.join(directory, f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = re.sub(r'<footer[^>]*>.*?</footer>', complex_footer, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated footer in {f}")
