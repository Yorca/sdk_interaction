import os

# Specify the directory path
directory = "/Volumes/YorcaDisk/class_apks"

# Loop through all files in the directory
for filename in os.listdir(directory):
    # Create the new filename by replacing spaces with no spaces
    new_filename = filename.replace("&", "")
    new_filename = filename.replace(" ", "")

    # Form the full file paths
    old_file = os.path.join(directory, filename)
    new_file = os.path.join(directory, new_filename)

    # Rename the files if the new filename is different
    if old_file != new_file:
        os.rename(old_file, new_file)