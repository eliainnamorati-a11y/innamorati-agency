with open("services.html", "r") as f:
    text = f.read()

# Update title
text = text.replace("<title>About | Innamorati Agency</title>", "<title>Services | Innamorati Agency</title>")

# Update hero
text = text.replace("We defy convention to accelerate business.", "Our Services")

# Remove team section and awards section
# They start after the last pathway block. Let's find the large landscape image separator and remove everything till the footer
start_str = "<!-- Large Landscape Image Separator -->"
end_str = "<!-- Massive Blue Footer -->"

start_idx = text.find(start_str)
end_idx = text.find(end_str)

if start_idx != -1 and end_idx != -1:
    text = text[:start_idx] + text[end_idx:]
    with open("services.html", "w") as f:
        f.write(text)
    print("Updated services.html")
else:
    print("Could not find sections to remove in services.html")
