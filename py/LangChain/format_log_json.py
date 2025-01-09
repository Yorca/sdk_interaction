import json
import os

folder = ""
des = ""

for filename in os.listdir(folder):
    with open(os.path.join(folder, filename), "r") as file:
        data = file.read()

    js_data = "[" + data[:-2] + "]"
    with open(os.path.join(des, filename), "a") as file:
        file.write(js_data)


