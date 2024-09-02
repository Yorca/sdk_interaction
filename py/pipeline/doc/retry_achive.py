import os
import time

import requests
import re

def save_webpage(url, name):

    # Fetch the webpage content
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Save the content to a file
        with open(f"website_retry/{name}.html", "w", encoding="utf-8") as file:
            file.write(response.text)
        time.sleep(3)
    else:
        print(f"Failed to fetch the webpage. url: {url} name:{name}")


with open("archive_log", "r") as file:
    lines = file.readlines()

for line in lines:
    if not line.startswith("Failed to fetch the webpage"):
        continue
    pattern = r'url:\s*(\S+)\s*name:(\S+)'
    match = re.findall(pattern, line)[0]
    save_webpage(match[0], match[1])
