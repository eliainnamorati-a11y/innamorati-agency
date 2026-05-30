import os
import glob

html_files = glob.glob('*.html')

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update Form
    content = content.replace(
        '<form class="footer-form">',
        '<form class="footer-form" action="https://formsubmit.co/elia@innamorati.ch" method="POST">'
    )
    content = content.replace(
        '<input type="text" placeholder="Your Name*">',
        '<input type="text" name="name" placeholder="Your Name*" required>'
    )
    content = content.replace(
        '<input type="email" placeholder="Your Email*">',
        '<input type="email" name="email" placeholder="Your Email*" required>'
    )
    content = content.replace(
        '<input type="text" placeholder="Phone Number">',
        '<input type="text" name="phone" placeholder="Phone Number">'
    )
    content = content.replace(
        '<input type="text" placeholder="Company Name">',
        '<input type="text" name="company" placeholder="Company Name">'
    )
    content = content.replace(
        '<input type="text" placeholder="Message*">',
        '<input type="text" name="message" placeholder="Message*" required>'
    )
    
    # Update Behance
    content = content.replace(
        '<li><a href="#">Behance</a></li>',
        '<li><a href="https://www.behance.net/innamoratiagency" target="_blank">Behance</a></li>'
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated {len(html_files)} files.")
