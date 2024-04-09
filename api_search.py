import subprocess
import os
import re

def decompile_apk(apk_path):
    output_dir = apk_path + "_decompiled"
    if os.path.exists(output_dir):
        return output_dir
    subprocess.run(["apktool", "d", apk_path, "-o", output_dir], check=True)
    return output_dir

def search_keyword_in_files(keyword, root_dir):
    keyword = keyword.lower()
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".smali"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read().lower()
                    if keyword in content:
                        print(content)
                        for match in re.finditer(rf'\.method.*?{keyword}.*?\n(.*?)\.end method', content, re.DOTALL):
                            yield os.path.relpath(file_path, root_dir), match.group(1)

def main(apk_path, keyword):
    decompiled_dir = decompile_apk(apk_path)
    print(f"Searching for keyword '{keyword}' in decompiled files...")
    for file_path, api_usage in search_keyword_in_files(keyword, decompiled_dir):
        print(f"Found in {file_path}:")
        print(api_usage)
        print("-" * 80)

if __name__ == "__main__":
    apk_path = "/Users/yorca/Downloads/Braindom_BrainGamesTest_2.3.2_Apkpure.apk"
    keyword = "mixedaudience"
    main(apk_path, keyword)
