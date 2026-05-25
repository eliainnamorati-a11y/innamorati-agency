with open("studio.html", "r") as f:
    text = f.read()

start_str = "<!-- CORE STAGGERING 3D GEOMETRY ENGINE -->"
end_str = "<!-- Large Landscape Image Separator -->"

start_idx = text.find(start_str)
end_idx = text.find(end_str)

if start_idx != -1 and end_idx != -1:
    text = text[:start_idx] + text[end_idx:]
    with open("studio.html", "w") as f:
        f.write(text)
    print("Updated studio.html successfully.")
else:
    print("Could not find boundaries.")
