with open("services.html", "r") as f:
    text = f.read()

start_str = "  <!-- Industries (Sticky Horizontal Scroll) -->\n  <section class=\"industries-section bg-dark\" id=\"industries-scroll-section\">"
end_str = "</section>\n\n  <!-- CORE STAGGERING 3D GEOMETRY ENGINE -->"

start_idx = text.find(start_str)
end_idx = text.find("</section>", start_idx) + len("</section>\n")

if start_idx != -1 and end_idx != -1:
    text = text[:start_idx] + text[end_idx:]
    with open("services.html", "w") as f:
        f.write(text)
    print("Removed Industries section from services.html")
else:
    print("Could not find boundaries")
