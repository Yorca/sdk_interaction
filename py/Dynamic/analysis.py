import json
import os

output = {}
for filename in os.listdir("log/apk_log"):
    if not filename.endswith(".log"):
        continue
    filepath = os.path.join("log/apk_log", filename)

    output[filename] = []
    with open(filepath, "r") as file:
        data = "[" + file.read()[:-2] + "]"
        print(filepath)

        js_data = json.loads(data)
    new_data = []
    for api_detail in js_data:
        new_data.append({
            "class": api_detail["class_name"],
            "method": api_detail['method'],
            "arguments": api_detail["arguments"]
        })
        if api_detail["is_privacy"]:
            output[filename].append(f"{api_detail['class_name']};{api_detail['method']}")
    output[filename] = list(set(output[filename]))
    if len(output[filename]) > 0:
        with open(f"log/priv_log/{filename}_new.log", "w") as file:
            file.write(json.dumps(new_data, indent=4))

# js_out = json.dumps(output, indent=4)
# with open("api_res.txt", "a") as file:
#     file.write(js_out)
