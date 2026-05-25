import os
import glob

old_footer = """<footer class="footer-blue reveal-up">
  <div class="footer-row-top">
    <div class="footer-col-left">
      <h2 class="footer-massive-text">Build Your New<br>Future With Us</h2>
    </div>
    <div class="footer-col-right">
      <p class="footer-desc">Innamorati Agency is a Geneva-based brand transformation studio helping organizations navigate growth, reinvention, and change through strategy, design, and digital.</p>
    </div>
  </div>
  
  <hr class="footer-divider">
  
  <div class="footer-row">
    <div class="footer-col-left">Sitemap</div>
    <div class="footer-col-right">
      <a href="index.html">Home</a>
      <a href="works.html">Case Studies</a>
      <a href="about.html">About</a>
      <a href="insights.html">Insights</a>
      <a href="contact.html">Contact</a>
    </div>
  </div>
  
  <hr class="footer-divider">
  
  <div class="footer-row">
    <div class="footer-col-left">Visit</div>
    <div class="footer-col-right">
      <p>Geneva Studio<br>Switzerland</p>
    </div>
  </div>
  
  <hr class="footer-divider">
  
  <div class="footer-row">
    <div class="footer-col-left">Work With Us</div>
    <div class="footer-col-right">
      <a href="mailto:elia@innamorati.ch">elia@innamorati.ch</a>
      <a href="#">Schedule a call</a>
    </div>
  </div>

  <div class="footer-marquee-container">
    <div class="footer-marquee-track">
      <img src="assets/logo-1.png" alt="Innamorati" class="footer-marquee-logo">
      <img src="assets/logo-1.png" alt="Innamorati" class="footer-marquee-logo">
      <img src="assets/logo-1.png" alt="Innamorati" class="footer-marquee-logo">
      <img src="assets/logo-1.png" alt="Innamorati" class="footer-marquee-logo">
      <!-- Duplicated for seamless infinite loop -->
      <img src="assets/logo-1.png" alt="Innamorati" class="footer-marquee-logo">
      <img src="assets/logo-1.png" alt="Innamorati" class="footer-marquee-logo">
      <img src="assets/logo-1.png" alt="Innamorati" class="footer-marquee-logo">
      <img src="assets/logo-1.png" alt="Innamorati" class="footer-marquee-logo">
    </div>
  </div>
</footer>"""

new_footer = """<footer class="footer-blue">
  <div class="footer-row-top reveal-up">
    <div class="footer-col-left">
      <h2 class="footer-massive-text">Build Your New<br>Future With Us</h2>
    </div>
    <div class="footer-col-right">
      <p class="footer-desc">Innamorati Agency is a Geneva-based brand transformation studio helping organizations navigate growth, reinvention, and change through strategy, design, and digital.</p>
    </div>
  </div>
  
  <hr class="footer-divider reveal-fade delay-1">
  
  <div class="footer-row reveal-up delay-1">
    <div class="footer-col-left">Sitemap</div>
    <div class="footer-col-right">
      <a href="index.html">Home</a>
      <a href="works.html">Case Studies</a>
      <a href="about.html">About</a>
      <a href="insights.html">Insights</a>
      <a href="contact.html">Contact</a>
    </div>
  </div>
  
  <hr class="footer-divider reveal-fade delay-2">
  
  <div class="footer-row reveal-up delay-2">
    <div class="footer-col-left">Visit</div>
    <div class="footer-col-right">
      <p>Geneva Studio<br>Switzerland</p>
    </div>
  </div>
  
  <hr class="footer-divider reveal-fade delay-3">
  
  <div class="footer-row reveal-up delay-3">
    <div class="footer-col-left">Work With Us</div>
    <div class="footer-col-right">
      <a href="mailto:elia@innamorati.ch">elia@innamorati.ch</a>
      <a href="#">Schedule a call</a>
    </div>
  </div>

  <div class="footer-single-logo-container reveal-up delay-4">
    <img src="assets/logo-1.png" alt="Innamorati" class="footer-single-logo">
  </div>
</footer>"""

html_files = glob.glob('*.html')
count = 0
for file in html_files:
    if file == 'index.html':
        continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_footer in content:
        content = content.replace(old_footer, new_footer)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
print(f"Updated footer in {count} files.")
