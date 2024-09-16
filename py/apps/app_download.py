from apkpure.apkpure import ApkPure

# Initialize the API
api = ApkPure()

# Search for an app and get top result
# top_result = api.search_top("tiktok")
# print(top_result)

# # Search for all results
# all_results = api.search_all("WhatsApp")
# print(all_results)
#
# Get app versions
# versions = api.get_versions("Instagram")
# print(versions)
#
# # Get app info
# app_info = api.get_info("WhatsApp")
# print(app_info)
#
# Download the latest version of an app
download_path = api.download("Instagram")
print(download_path)
#
# # Download a specific version of an app
# api.download("WhatsApp", version="2.21.1.15")