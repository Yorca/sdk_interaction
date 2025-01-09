
import ast
import json
import re
with open("res/forbidden2.log", "r") as file:
    lines = file.read().split('\n')
    contents = []
    forbids = []
    for line in lines:
        if line.startswith("Content:"):
            content = line.removeprefix('Content:')
            if "not found" in content.lower():
                contents.append([])
            else:
                contents.append(ast.literal_eval(content))
        elif line.startswith("result:"):
            content = line.removeprefix('result:')
            if "not found" in content.lower():
                forbids.append([])
            else:
                items = ast.literal_eval(content)
                for i in range(len(items)):
                    pattern = r"\(Pattern \d+\)"
                    items[i] = re.sub(pattern, "", items[i]).strip()
                forbids.append(items)
    print(contents)
    print(len(contents))
    print(len(forbids))
    data = []
    for i in range(len(contents)):
        data.append({
            "content": contents[i],
            "forbidden": forbids[i]
        })
    print(data)
    js_data = json.dumps(data, indent=4)
    with open("data/forbiddens.log", "w") as file:
        file.write(js_data)