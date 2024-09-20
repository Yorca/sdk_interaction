#!/bin/bash

# Terminate the previous running script if any
pkill -f "/home/zh844971/sdk_interaction/sdk_interaction/py/apk_downloader/downloader_v2.py"

# Run the script
python3 /home/zh844971/sdk_interaction/sdk_interaction/py/apk_downloader/downloader_v2.py &