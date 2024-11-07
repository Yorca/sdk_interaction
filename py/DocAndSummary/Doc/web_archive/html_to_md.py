import html2text
import os
import email
from html.parser import HTMLParser

directory = "privacy_docs3.0"

def read_and_parse_mhtml(file_path):
    with open(file_path, 'r', encoding='iso-8859-1') as f:
        mhtml_content = f.read()
    msg = email.message_from_string(mhtml_content)

    for part in msg.walk():
        if part.get_content_type() == "text/html":
            html_content = part.get_payload(decode=True).decode('iso-8859-1')

    parser = HTMLParser()
    parser.feed(html_content)

    return html_content


for htmlfile in os.listdir("privacy_docs3.0"):
    html_content = ""
    path = f"{directory}/{htmlfile}"
    if htmlfile.endswith(".html"):
        with open(path, 'r', encoding='utf-8') as html_file:
            html_content = html_file.read()
    elif htmlfile.endswith(".mhtml"):
        html_content = read_and_parse_mhtml(path)

    markdown_content = html2text.html2text(html_content)
    name = htmlfile.replace(".html", ".md").replace(".mhtml", ".md")
    with open(f'privacy_doc_md/{name}', 'w', encoding='utf-8') as md_file:
        md_file.write(markdown_content)

