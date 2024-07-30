import re
import json

with open('notifyFlowOut_new.txt', 'r') as file:
    data = file.read()

details = data.split('\n\n')


for detail in details:
    if "backward Method List" not in detail:
        continue
    privacy_api_match = re.search(r'Privacy API:\s+<(.+):\s+(.+)>', detail)
    privacy_api_class = privacy_api_match.group(1)
    privacy_api_method = privacy_api_match.group(2)
    if "setIsAgeRestrictedUser" not in privacy_api_method:
        continue
    backward_methods = re.findall(r'Method<(.+):\s+(.+)>', data)
    backward_method_list = [{'class': m[0], 'method': m[1]} for m in backward_methods]
    print("backward list\n")
    for method in backward_method_list:
        print(f"Class: {method['class']}, Method: {method['method']}")


