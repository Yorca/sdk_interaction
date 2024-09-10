from openai import OpenAI
from bs4 import BeautifulSoup
import os
import json

def read_and_parse_html(file_path):
    # Read your HTML file
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse HTML using Beautiful Soup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Example: Extract text or specific elements
    text_content = soup.get_text(separator=' ', strip=True)
    return text_content

<<<<<<< HEAD:py/DocAnalysis/parse_html.py
print(read_and_parse_html('website_html/Fyber(Digital Turbine)_gdpr_ccpa_coppa.html'))
=======
print(read_and_parse_html('website_html/AppLovin_gdpr_ccpa_coppa.html'))
>>>>>>> refs/remotes/origin/main:DocAnalysis/parse_html.py
