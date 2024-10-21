import requests
from bs4 import BeautifulSoup

# Replace with the URL you want to scrape
url = 'https://play.google.com/store/apps/datasafety?id=com.iz.coloring.games.kids.drawing.book.color.by.number&hl=en&gl=us'

# Send a GET request to the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup)

    # Extract specific information (for example, all headings)
    headings = soup.find_all('h1')  # You can change 'h1' to other tags like 'p', 'a', etc.

    # Print the extracted information
    for heading in headings:
        print(heading.get_text())
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
