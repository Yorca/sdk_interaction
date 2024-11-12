import os

# Specify the directory path
directory = "/Volumes/T7 Shield/apps"

# Loop through all files in the directory
for filename in os.listdir(directory):
    # Create the new filename by replacing spaces with no spaces
    if not filename.endswith(".XAPK") and not filename.endswith(".APK"):
        continue
    new_filename = filename.replace(".XAPK", ".xapk").replace(".APK", ".apk")
    # new_filename = filename.replace(".APK", ".apk")
    print(new_filename)
    # Form the full file paths
    old_file = os.path.join(directory, filename)
    new_file = os.path.join(directory, new_filename)
    # # Rename the files if the new filename is different
    # if old_file != new_file:
    #     print(old_file)
    #     print(new_file)
    #     os.rename(old_file, new_file)