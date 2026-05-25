import os

case_studies = [
    {
        "filename": "hanseatic.html",
        "title": "Hanseatic",
        "desc_1": "Hanseatic builds technology that makes physical supply chains programmable. The company enables seamless, transparent execution of physical energy trading by turning complex contractual, logistical, and settlement processes into automated, verifiable workflows.",
        "desc_2": "Innamorati developed the full brand foundation for Hanseatic, including logo design, visual identity, and core brand assets. The identity system was designed to scale across digital and physical touchpoints, ensuring consistency and clarity while reflecting the company’s technological rigor, reliability, and forward-looking approach to energy trading.",
        "industry": "Energy",
        "location": "Geneva, Switzerland",
        "year": "2024",
        "services": ["Logo Design", "Story & Messaging", "Brand Identity", "Website Design"],
        "hero_image": "hanseatic/Generated-Image-January-11-2026-12_45PM-scaled.webp",
        "images": [
            "hanseatic/Generated-Image-January-15-2026-9_46PM-copy-2-scaled.webp",
            "hanseatic/Generated-Image-January-15-2026-9_46PM-copy-scaled.webp",
            "hanseatic/Presentacion-copy.webp",
            "hanseatic/Generated-Image-January-11-2026-10_31PM.webp",
            "hanseatic/de475c34-81f9-4587-97b5-4459984dd855.webp",
            "hanseatic/Tarjetas-copy-1.webp",
            "hanseatic/hanseatic-final-13.webp",
            "hanseatic/hanseatic-final-5-scaled.webp"
        ]
    },
    {
        "filename": "domaine-de-bellevue.html",
        "title": "Domaine de Bellevue",
        "desc_1": "At a sought-after address in the peaceful hills of Trélex, a rare collection of eight exceptional villas unfolds. Designed as a true private estate, this project combines refinement, discretion, and high-end comfort. Nestled in a lush green setting, some villas even enjoy unobstructed views of Lake Geneva, offering an exclusive and harmonious living environment.",
        "desc_2": "We crafted a distinctive brand identity and visual language that mirrors this architectural elegance and understated luxury. From logo design to digital storytelling, every element was conceived to express the estate’s refinement and exclusivity. The website was designed to immerse visitors in the serene atmosphere of Trélex.",
        "industry": "Real Estate",
        "location": "Trélex, Switzerland",
        "year": "2023",
        "services": ["Logo Design", "Website Design", "Brochure Design", "Story & Messaging"],
        "hero_image": "domaine de bellevue/01_Domenda-Bellevue_height2250-1.webp",
        "images": [
            "domaine de bellevue/02_Domenda-Bellevue_height2250.webp",
            "domaine de bellevue/03_Domenda_Bellevue_cropped_triple-scaled.webp",
            "domaine de bellevue/04_Domenda-Bellevue_height2250.webp",
            "domaine de bellevue/domaine-1.webp",
            "domaine de bellevue/image01_final-copy.webp",
            "domaine de bellevue/image05_sejour-2_final-scaled.webp",
            "domaine de bellevue/image10_area_HD_V2-scaled.webp"
        ]
    },
    {
        "filename": "jacobco.html",
        "title": "Jacob & Co",
        "desc_1": "Extending heritage into a smarter way to move through time. Jacob & Co represents the pinnacle of luxury watchmaking, blending complex mechanics with striking visual design.",
        "desc_2": "We led the digital strategy and experience design for Jacob & Co, creating an immersive web presence that showcases the intricate details of their timepieces while providing a seamless luxury shopping experience for high-net-worth clients.",
        "industry": "Luxury & Watches",
        "location": "Geneva, Switzerland",
        "year": "2024",
        "services": ["Digital Strategy", "Digital Experience", "UI/UX Design"],
        "hero_image": "assets/watch-1.jpg",
        "images": []
    },
    {
        "filename": "rolls-royce.html",
        "title": "Rolls Royce Motor Cars",
        "desc_1": "Rolls-Royce Motor Cars stands globally for unparalleled luxury, engineering excellence, and automotive perfection.",
        "desc_2": "We were commissioned to create a high-end CGI video to mark the grand opening of Rolls-Royce’s new dealership in Geneva. The video captures the essence of the brand, blending dynamic 3D animation with the prestige of Rolls-Royce.",
        "industry": "Automotive",
        "location": "Geneva, Switzerland",
        "year": "2023",
        "services": ["3D Animation", "CGI Video", "Art Direction"],
        "hero_image": "rolls royce/rollsvideocropped (1).mp4",
        "images": []
    },
    {
        "filename": "cleo.html",
        "title": "Cleo",
        "desc_1": "Cleo is an innovative brand stepping into the fashion space with elegance and modernity. The brand focuses on premium aesthetics and a distinctive product lineup.",
        "desc_2": "We provided a refined brand identity and modern digital presence for Cleo. By creating a cohesive visual language and elegant web design, we helped establish Cleo as a sophisticated player in its market.",
        "industry": "Fashion & Accessories",
        "location": "Miami, USA",
        "year": "2024",
        "services": ["Brand Identity", "Web Design", "Visual Strategy"],
        "hero_image": "cleo/Bolsa-Cleo-03-scaled.webp",
        "images": [
            "cleo/Website-Mockup-scaled.webp",
            "cleo/Elegance.webp",
            "cleo/image-in-sand-copy-3.webp",
            "cleo/Untitled-design-13-scaled.webp",
            "cleo/Logo-Cleo-scaled.webp",
            "cleo/Untitled-design-10-scaled.webp"
        ]
    },
    {
        "filename": "pley-by-ney.html",
        "title": "Pley by Ney",
        "desc_1": "Pley by Ney offers an immersive branding experience that captures a modern, dynamic aesthetic. It connects deeply with audiences through striking visuals and bold strategy.",
        "desc_2": "We developed the brand strategy and visual identity for Pley by Ney, ensuring every touchpoint from digital to physical embodies their modern aesthetic and energetic vision.",
        "industry": "Sports & Lifestyle",
        "location": "Miami, USA",
        "year": "2024",
        "services": ["Brand Strategy", "Visual Identity", "Art Direction"],
        "hero_image": "pley/pley-by-ney.webp",
        "images": [
            "pley/billboard_cropped_same_ratio.webp",
            "pley/soccer_cropped_1279x723_ratio.webp"
        ]
    },
    {
        "filename": "isigna-wealth.html",
        "title": "Isigna Wealth",
        "desc_1": "Isigna Wealth is a boutique financial advisory firm dedicated to preserving and growing wealth for high-net-worth individuals and families through bespoke strategies.",
        "desc_2": "We crafted a premium brand identity and digital platform that reflects trust, exclusivity, and financial acumen. The design language emphasizes stability and personalized service.",
        "industry": "Finance & Wealth",
        "location": "Geneva, Switzerland",
        "year": "2023",
        "services": ["Brand Strategy", "Logo Design", "Web Design"],
        "hero_image": "le tual/case-study-1.webp",
        "images": []
    }
]

def render_hero_image(src):
    if src.endswith('.mp4'):
        return f'<video src="{src}" autoplay loop muted playsinline style="width: 100%; height: 100%; object-fit: cover;"></video>'
    else:
        return f'<img src="{src}" alt="Hero Image" style="width: 100%; height: 100%; object-fit: cover;">'

def render_gallery(images, desc_2):
    html = ''
    if not images:
        html += f'''
      <div class="project-text-block reveal-up" style="margin: 6vw auto 4vw auto; max-width: 900px; padding: 0 5vw;">
        <h3 style="font-size: 1.5rem; font-weight: 400; margin-bottom: 1.5rem; color: #111;">Our Project</h3>
        <p style="font-size: 1.25rem; line-height: 1.6; color: #444; margin: 0;">{desc_2}</p>
      </div>'''
        return html
    
    # First image is horizontal
    html += f'''
      <!-- 1 Horizontal -->
      <div class="slide-reveal-mask" style="width: 100%; margin-top:2vw; border-radius:4px; aspect-ratio: 16/9;">{render_hero_image(images[0])}</div>
      
      <div class="project-text-block reveal-up" style="margin: 6vw auto 4vw auto; max-width: 900px; padding: 0 5vw;">
        <h3 style="font-size: 1.5rem; font-weight: 400; margin-bottom: 1.5rem; color: #111;">Our Project</h3>
        <p style="font-size: 1.25rem; line-height: 1.6; color: #444; margin: 0;">{desc_2}</p>
      </div>
'''
    i = 1
    while i < len(images):
        if i + 1 < len(images):
            # 2 Vertical
            html += f'''
      <!-- 2 Vertical -->
      <div class="gallery-row" style="display: grid; grid-template-columns: 1fr 1fr; gap: 2vw; margin-top:2vw;">
        <div class="slide-reveal-mask" style="width: 100%; height: 100%; aspect-ratio: 4/5; border-radius:4px;">{render_hero_image(images[i])}</div>
        <div class="slide-reveal-mask" style="width: 100%; height: 100%; aspect-ratio: 4/5; border-radius:4px;">{render_hero_image(images[i+1])}</div>
      </div>
'''
            i += 2
            if i < len(images):
                # 1 Horizontal
                html += f'''
      <!-- 1 Horizontal -->
      <div class="slide-reveal-mask" style="width: 100%; margin-top:2vw; border-radius:4px; aspect-ratio: 16/9;">{render_hero_image(images[i])}</div>
'''
                i += 1
        else:
            # Only 1 image left
            html += f'''
      <!-- 1 Horizontal -->
      <div class="slide-reveal-mask" style="width: 100%; margin-top:2vw; border-radius:4px; aspect-ratio: 16/9;">{render_hero_image(images[i])}</div>
'''
            i += 1
    
    return html

def get_template(data):
    services_html = "".join([f"<li>{s}</li>" for s in data['services']])
    
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{data['title']} | Innamorati Agency</title>
  <link rel="stylesheet" href="style.css" />
  <style>
    /* Specific styles for the project pages */
    .project-header {{
      padding: 15vw 5vw 5vw 5vw;
      background-color: var(--bg-light);
    }}
    .project-title {{
      font-family: var(--font-serif);
      font-size: 5vw;
      line-height: 1;
      letter-spacing: -0.02em;
      font-weight: 300;
      margin-bottom: 2rem;
    }}
    .project-meta {{
      display: flex;
      gap: 4rem;
      margin-bottom: 5vw;
      font-size: 1.1rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      align-items: flex-start;
    }}
    .meta-item > span {{
      display: block;
      color: #888;
      font-size: 0.85rem;
      margin-bottom: 1rem;
      letter-spacing: 0.05em;
    }}
    .meta-item .project-tags {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.5rem;
      text-transform: none;
      letter-spacing: normal;
      margin-top: 0;
    }}
    @media (max-width: 768px) {{
      .project-meta {{
        flex-direction: column;
        gap: 2rem;
      }}
      .meta-item .project-tags {{
        grid-template-columns: 1fr;
      }}
    }}
    .project-body {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 5vw;
      padding: 5vw;
      background-color: var(--bg-light);
    }}
    .project-text h3 {{
      font-size: 1.5rem;
      margin-bottom: 1.5rem;
      font-weight: 500;
    }}
    .project-text p {{
      font-size: 1.25rem;
      line-height: 1.6;
      color: #333;
      margin-bottom: 2rem;
    }}
    .project-gallery {{
      padding: 5vw;
      background-color: var(--bg-light);
      display: flex;
      flex-direction: column;
      gap: 2vw;
    }}
    .project-gallery img {{
      width: 100%;
      border-radius: 4px;
    }}
    .placeholder-img {{
      width: 100%;
      height: 60vh;
      background-color: #e0e0e0;
      border-radius: 4px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #888;
      font-size: 1.2rem;
    }}
    @media (max-width: 768px) {{
      .project-body {{
        grid-template-columns: 1fr;
      }}
    }}
  </style>
</head>
<body>
  <!-- Floating Glass Navigation -->
    <nav class="navbar-pill light-theme">
    <div class="logo"><a href="index.html"><img src="assets/logo-1.png" alt="Innamorati Agency" style="height: 29px;"></a></div>
    <ul class="nav-links">
      <li><a href="works.html">Case Studies</a></li>
      <li><a href="about.html">About</a></li>
      <li><a href="insights.html">Insights</a></li>
      <li><a href="contact.html">Contact</a></li>
    </ul>
    <div class="hamburger"><span></span><span></span></div>
  </nav>

  <main>
    <section class="project-hero" style="display: flex; flex-wrap: wrap; min-height: 100vh; padding-top: 80px; background-color: var(--bg-light);">
      <div class="project-hero-left" style="flex: 1; min-width: 300px; padding: 5vw; display: flex; flex-direction: column; justify-content: center;">
        <h1 class="project-title" style="margin-top: 0; line-height: 1.1; margin-bottom: 2rem;">{data['title']}</h1>
        
        <div class="project-description" style="font-size: 1.1rem; line-height: 1.6; color: #555; max-width: 600px; margin-bottom: 4rem;">
          <p>{data['desc_1']}</p>
        </div>

        <div class="project-meta-flex" style="display: flex; flex-wrap: wrap; gap: 3rem;">
          <div class="meta-left" style="flex: 1; display: flex; flex-direction: column; gap: 2.5rem; min-width: 200px;">
            <div class="meta-item">
              <h3 style="font-weight: 300; font-size: 1.5rem; margin-bottom: 0.8rem; color: #333;">Industry</h3>
              <p style="color: #777; margin: 0;">{data['industry']}</p>
            </div>
            <div class="meta-item">
              <h3 style="font-weight: 300; font-size: 1.5rem; margin-bottom: 0.8rem; color: #333;">Location</h3>
              <p style="color: #777; margin: 0;">{data['location']}</p>
            </div>
            <div class="meta-item">
              <h3 style="font-weight: 300; font-size: 1.5rem; margin-bottom: 0.8rem; color: #333;">Year</h3>
              <p style="color: #777; margin: 0;">{data['year']}</p>
            </div>
          </div>
          <div class="meta-right" style="flex: 1; min-width: 200px;">
            <div class="meta-item">
              <h3 style="font-weight: 300; font-size: 1.5rem; margin-bottom: 0.8rem; color: #333;">Services</h3>
              <ul style="list-style: none; padding: 0; margin: 0; color: #777; line-height: 2;">
                {services_html}
              </ul>
            </div>
          </div>
        </div>
      </div>
      
      <div class="project-hero-right" style="flex: 1; min-width: 300px;">
        {render_hero_image(data['hero_image'])}
      </div>
    </section>

    <section class="project-gallery">
{render_gallery(data['images'], data['desc_2'])}
    </section>
  </main>

  <!-- Bright Blue Footer -->
      <footer class="footer-complex">
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
  </footer>

  <script src="main.js"></script>

<!-- Full Screen Menu Overlay -->
<div class="full-screen-menu">
  <div class="menu-top">
    <div class="logo"><a href="index.html" style="color:inherit; text-decoration:none;"><img src="assets/logo-1.png" alt="Innamorati Agency" style="height: 29px;"></a></div>
    <div class="menu-close">✕</div>
  </div>
  <div class="menu-content">
    <span class="menu-label">Menu</span>
    <ul class="menu-links">
      <li><a href="works.html">Case Studies</a></li>
      <li><a href="about.html">About</a></li>
      <li><a href="insights.html">Insights</a></li>
      <li><a href="contact.html">Contact</a></li>
    </ul>
  </div>
    <div class="menu-footer">
    <div class="menu-footer-block">
      <span>Visit</span>
      <p>Geneva &amp; Miami</p>
    </div>
    <div class="menu-footer-block">
      <span>Work With Us</span>
      <a href="mailto:elia@innamorati.ch">elia@innamorati.ch</a>
      <a href="contact.html">Schedule a call</a>
    </div>
  </div>
</div>
</body>
</html>
"""

def generate_files():
    for cs in case_studies:
        content = get_template(cs)
        with open(cs['filename'], 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Generated {cs['filename']}")

if __name__ == "__main__":
    generate_files()
