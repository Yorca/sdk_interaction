#!/bin/bash

# Terminate the previous running script if any
pkill -f "/Users/yorca/projects/sdk_interaction/py/apk_downloader/downloader_v5.py"

# Run the script
/Users/yorca/projects/sdk_interaction/py/myenv/bin/python3.12 /Users/yorca/projects/sdk_interaction/py/apk_downloader/downloader_v5.py &