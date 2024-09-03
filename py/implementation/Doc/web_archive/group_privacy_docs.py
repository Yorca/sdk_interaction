import os
import shutil


def group_and_copy_files(source_dir, dest_dir):

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for filename in os.listdir(source_dir):
        if os.path.isfile(os.path.join(source_dir, filename)):
            #extract the SDK name
            sdkname = filename.split('_')[0]

            # Create a directory for the SDK if it doesn't exist
            sdk_dir = os.path.join(dest_dir, sdkname)
            if not os.path.exists(sdk_dir):
                os.makedirs(sdk_dir)

            # Copy the file to the SDK directory
            shutil.copy(os.path.join(source_dir, filename), sdk_dir)


# Usage
source_directory = 'privacy_docs'
destination_directory = 'privacy_docs_group'

group_and_copy_files(source_directory, destination_directory)
