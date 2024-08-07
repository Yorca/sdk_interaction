import json
import os
# Read the JSON data from the file
# with open("response_selected/AppLovin_setHasUserConsent.json", 'r') as file:
#     json_str = file.read()
# print(json_str)
# actual_json_str = json.loads(json_str)[0]
#
# # Load the JSON data from the decoded string
# json_data = json.loads(actual_json_str)
# # Beautify the JSON data
# beautified_json = json.dumps(json_data, indent=4)
#
# print(beautified_json)

# # Write the beautified JSON to a new file
# with open(output_file_path, 'w') as file:
#     file.write(beautified_json)


# Read the JSON string from the file
with open("response_selected/AppLovin_setHasUserConsent.json", 'r') as file:
    json_str = file.read()

# The JSON string contains a list with a single string element that represents the JSON object.
# Extract the first element from the list and decode the JSON string.
actual_json_str = json.loads(json_str)[0]

# Load the JSON data from the decoded string
json_data = json.loads(actual_json_str)

# Beautify the JSON data
beautified_json = json.dumps(json_data, indent=4, ensure_ascii=False)
print(beautified_json)
#
# print(f'Beautified JSON has been saved to {output_file_path}')
#
# folder_path = "responses2"
# for filename in os.listdir(folder_path):
#     file_path = os.path.join(folder_path, filename)
#
#     # 仅处理文件，不处理文件夹
#     if os.path.isfile(file_path):
#         with open(file_path, 'r') as file:
#             json_str = file.read()
#
#         # 对文件内容进行更改的示例（此处是将所有字母转换为大写）
#         actual_json_str = json.loads(json_str)[0]
#
#         # Load the JSON data from the decoded string
#         json_data = json.loads(actual_json_str)
#         # Beautify the JSON data
#         beautified_json = json.dumps(json_data, indent=4)
#
#         # 将修改后的内容覆盖写回文件
#         with open(file_path, 'w', encoding='utf-8') as file:
#             file.write(beautified_json)
#         print(f'File {filename} has been modified and saved.')