import os
import shutil


def copy_privacy_files(source_directory):
    destination_directory = 'web_archive'

    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    for filename in os.listdir(source_directory):
        if "privacy" in filename:
            file_path = os.path.join(source_directory, filename)
            if os.path.isfile(file_path):
                shutil.copy(file_path, destination_directory)
                print(f"Copied: {filename} to {destination_directory}")

copy_privacy_files("website")
copy_privacy_files("website_sup")
