import subprocess
import os
import re


def decompile_apk(apk_path):
    output_dir = apk_path + "_decompiled"
    if os.path.exists(output_dir):
        return output_dir
    subprocess.run(["apktool", "d", apk_path, "-o", output_dir], check=True)
    return output_dir


def search_method_in_files(method_name, class_name, root_dir):
    method_name_pattern = rf'\.method.*?\b{re.escape(method_name)}\b.*?\n(.*?)\.end method'
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".smali"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if re.search(method_name_pattern, content, re.DOTALL):
                        class_pattern = r'L(.*?);'  # Matches class definitions in smali files
                        class_matches = re.findall(class_pattern, content)
                        if class_matches:
                            class_full_name = class_matches[0].replace('/', '.')
                            class_last_element = class_full_name.split('.')[-1]
                            # Check if class_name matches the last element or is empty
                            if not class_name or class_last_element == class_name:
                                print(content)
                                yield class_full_name



def main(apk_path, method_name, class_name=""):
    decompiled_dir = decompile_apk(apk_path)
    print(f"Searching for method '{method_name}' in decompiled files...")
    matched_classes = set(search_method_in_files(method_name, class_name, decompiled_dir))

    if matched_classes:
        print("Matched class names:")
        for class_name in matched_classes:
            print(class_name)
    else:
        print("No matching classes found.")


if __name__ == "__main__":
    apk_path = "/Users/yorca/Downloads/Braindom_BrainGamesTest_2.3.2_Apkpure.apk"
    method_name = "setIsAgeRestrictedUser"
    class_name = ""
    main(apk_path, method_name, class_name)
