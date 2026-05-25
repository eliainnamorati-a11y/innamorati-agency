import os

filepath = "/Users/eliainnamorati/Desktop/innamorati-agency-final/studio.html"

with open(filepath, "r") as f:
    text = f.read()

start_marker = "  <!-- Industries (Sticky Horizontal Scroll) -->"
end_marker = "</section>\n\n  <!-- Large Landscape Image Separator -->"

start_idx = text.find(start_marker)
end_idx = text.find("</section>", start_idx) + len("</section>")

if start_idx != -1 and end_idx != -1:
    new_html = """  <!-- Introduction Section -->
  <section class="studio-intro-section" style="background-color: var(--bg-dark); color: white; padding: 10vw 5vw;">
    <div style="display: flex; flex-wrap: wrap; gap: 5vw; max-width: 1200px; margin: 0 auto 8vw auto;">
      <div style="flex: 0 0 200px;">
        <span class="label-muted" style="color: rgba(255,255,255,0.6);">INTRODUCTION</span>
      </div>
      <div style="flex: 1; min-width: 300px;">
        <p style="font-family: var(--font-serif); font-size: clamp(1.2rem, 1.5vw, 1.4rem); line-height: 1.6; color: rgba(255,255,255,0.8); margin-bottom: 2rem; font-weight: 300;">
          The Innamorati studio opened in 2024, after decades of global design & marketing experience working alongside some of the world's most successful & prestigious brands on behalf of other leading agencies.
        </p>
        <p style="font-family: var(--font-serif); font-size: clamp(1.2rem, 1.5vw, 1.4rem); line-height: 1.6; color: rgba(255,255,255,0.8); font-weight: 300;">
          Our blend of strategy & creativity results in dynamic outcomes that assist in supporting the future growth of our clients' businesses. Everything we achieve is repeatedly delivered efficiently through commitment, sincerity & unconditional professionalism.
        </p>
      </div>
    </div>

    <div style="display: flex; gap: 2vw; max-width: 1400px; margin: 0 auto; height: 60vh;">
      <div style="flex: 4; height: 100%;">
        <img src="assets/office_det.png" alt="Studio Detail" style="width: 100%; height: 100%; object-fit: cover;">
      </div>
      <div style="flex: 8; height: 100%;">
        <img src="assets/office_int.png" alt="Studio Interior" style="width: 100%; height: 100%; object-fit: cover;">
      </div>
    </div>
  </section>"""
    
    text = text[:start_idx] + new_html + text[end_idx:]
    
    with open(filepath, "w") as f:
        f.write(text)
    print("Replaced Industries section with Introduction section.")
else:
    print("Could not find start/end indices for replacement.")
