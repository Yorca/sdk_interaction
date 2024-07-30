import requests

# Replace with your desired URL
url = "https://developers.applovin.com/en/android/overview/privacy/"

# Fetch the webpage content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Save the content to a file
    with open("cached_page.html", "w", encoding="utf-8") as file:
        file.write(response.text)
    print("Webpage cached successfully!")
else:
    print("Failed to fetch the webpage.")