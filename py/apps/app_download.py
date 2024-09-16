import requests
from bs4 import BeautifulSoup
import re


def download_apk(package_name):
    base_url = f"https://apkpure.com/search?q={package_name}"

    # Step 1: Get search results
    search_page = requests.get(base_url)
    print(search_page)
    soup = BeautifulSoup(search_page.content, 'html.parser')

    # Step 2: Find the app page URL
    app_page = soup.find("a", href=re.compile(f"/{package_name}"))
    if not app_page:
        print(f"Package '{package_name}' not found.")
        return

    app_url = "https://apkpure.com" + app_page['href']

    # Step 3: Go to the app page and find the download button
    app_page_response = requests.get(app_url)
    app_soup = BeautifulSoup(app_page_response.content, 'html.parser')

    # Get download link for the latest version
    download_button = app_soup.find("a", {"id": "download_link"})
    if not download_button:
        print(f"Could not find download link for '{package_name}'.")
        return

    # Get the APK download URL
    download_url = download_button['href']

    # Step 4: Download the APK file
    apk_response = requests.get(download_url, stream=True)
    if apk_response.status_code == 200:
        apk_file_path = f"{package_name}.apk"
        with open(apk_file_path, 'wb') as apk_file:
            for chunk in apk_response.iter_content(chunk_size=1024):
                if chunk:
                    apk_file.write(chunk)
        print(f"APK for '{package_name}' downloaded successfully.")
    else:
        print(f"Failed to download APK for '{package_name}'.")


# Example usage:
package_name = 'com.facebook.katana'  # Replace this with the package name you want
download_apk(package_name)