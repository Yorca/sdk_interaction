import os
import subprocess
import re
import pandas as pd
import time
import frida
import json
import threading
from datetime import datetime
import zipfile
import shutil
import time
import re
import xml.etree.ElementTree as ET

install_failed = False

def parse_page_xml():
    """Dumps the current UI XML and parses it."""
    result = subprocess.run(['adb', 'shell', 'uiautomator', 'dump'], capture_output=True, text=True)
    print(result.stdout)
    dump_path_match = re.search(r'/sdcard/.*\.xml', result.stdout)

    if dump_path_match:
        dump_path = dump_path_match.group(0)
        subprocess.run(['adb', 'pull', dump_path, 'page_dump.xml'], capture_output=True)

        # Parse the XML file
        try:
            tree = ET.parse('page_dump.xml')
            root = tree.getroot()
            nodes = root.findall(".//node")
            return nodes
        except Exception as e:
            print(f"Error parsing XML: {str(e)}")
            return None
    else:
        print("Failed to get UI dump.")
        return None

def get_node_bounds(node):
    """Extracts the bounds from a node in the UI dump."""
    bounds = node.attrib.get('bounds', '')
    match = re.match(r"\[(\d+),(\d+)\]\[(\d+),(\d+)\]", bounds)
    if match:
        x1, y1, x2, y2 = map(int, match.groups())
        return (x1 + x2) // 2, (y1 + y2) // 2
    return None

def click_by_adb(x, y):
    """Performs an ADB tap action on the screen at the specified coordinates."""
    subprocess.run(['adb', 'shell', 'input', 'tap', str(x), str(y)])


def click_pop_window_by_xml(expect_texts):
    """Handles pop-up windows during APK installation by clicking the expected text."""
    for expect_text in expect_texts:
        count = 10
        while count > 0:
            if install_failed:
                print("install_failed!")
                break
            nodes = parse_page_xml()
            if nodes is None:
                print("Failed to get XML data. Retrying...")
                time.sleep(1)
                continue

            found = False
            for node in nodes:
                actual_text = node.attrib.get('text', '').encode('utf-8').decode('utf-8')
                if actual_text == expect_text:
                    x, y = get_node_bounds(node)
                    if x and y:
                        click_by_adb(x, y)
                        found = True
                        break
            if found:
                break
            time.sleep(1)
            count -= 1
            if count == 0:
                break

def extract_xapk(xapk_file, output_dir):
    """Extracts the XAPK file and returns the extracted file name."""
    if zipfile.is_zipfile(xapk_file):
        with zipfile.ZipFile(xapk_file, 'r') as zip_ref:
            zip_ref.extractall(output_dir)
            extracted_files = zip_ref.namelist()  # List of all extracted files
            print(f"Extracted {xapk_file} to {output_dir}")
            return extracted_files  # Return the list of extracted file names
    else:
        print(f"{xapk_file} is not a valid XAPK file.")
        return None


def log_error(TAG, err):
    date_str = str(datetime.now())
    with open("log/error.log", "a") as file:
        file.write(f"------------------------{date_str}\n  TAG:{TAG}\n  Error:{err}\n")


def get_apk_package_name(apk_path):
    try:
        result = subprocess.run(['aapt', 'dump', 'badging', apk_path], capture_output=True, text=True, check=True)
        output_lines = result.stdout.split('\n')
        for line in output_lines:
            if line.startswith('package: name='):
                package_name = re.search(r"name='(.*?)'", line).group(1)
                return package_name
        raise ValueError('Package name not found in the APK.')
    except Exception as e:
        log_error("Get Package Name Failed", f"apk:{apk_path}, {str(e)}")
        return None

def get_script_code(package_name):
    hook_methods = loadAllMethods()
    class_list = loadAllClasses()
    overload = f"""
    Java.perform(function () {{
        Java.deoptimizeEverything()
        function hookMethod(cls_name, methodName, pkg, source) {{
            try {{
                var clazz = Java.use(cls_name);
                if (!clazz) {{
                    return;
                }}
                var overloadCount = clazz[methodName]?.overloads?.length;
                if (!overloadCount || overloadCount <= 0) {{
                    return;
                }}
                for (var i = 0; i < overloadCount; i++) {{
                    (function () {{
                        var originalMethod = clazz[methodName].overloads[i];
                        originalMethod.implementation = function () {{
                            send({{
                                type: 'log',
                                source: source,
                                method: methodName,
                                package_name: pkg,
                                class_name: cls_name,
                                timestamp: new Date().getTime(),
                                ref: this + '',
                                arguments: JSON.stringify(arguments),
                                stack_trace: Java.use('android.util.Log').getStackTraceString(Java.use('java.lang.Exception').$new())
                            }});
                            var result = originalMethod.apply(this, arguments);
                            return result;
                        }};
                    }})();
                }}
            }} catch (e) {{
                send({{
                    type: 'error',
                    source: source,
                    method: methodName,
                    package_name: pkg,
                    class_name: cls_name,
                    timestamp: new Date().getTime(),
                    error: "" + e              
                }});
            }}
        }}
    """

    # for hook_method in hook_methods:
    #     cls_name = hook_method["Class"].strip()
    #     mtd_name = hook_method["API"].strip()
    #     overload += f"""
    #     hookMethod("{cls_name}", "{mtd_name}", "{package_name}", "method");
    #     """

    for cls in class_list:
        cls = cls.strip()
        print(cls)
        overload += f"""
                    try {{
                        var clazz = Java.use("{cls}");
                        console.log("clazz = " + clazz)
                        if (clazz) {{
                            var methods = clazz.class.getDeclaredMethods();
                            console.log("methods = " + methods)
                            for (var i = 0; i < methods.length; i++) {{
                                var methodName = methods[i].getName();
                                if (methodName === "$new") {{
                                    methodName = "$init";
                                }}
                                else if (methodName.startsWith("$")) {{
                                    continue;
                                }}
                                hookMethod("{cls}", methodName, "{package_name}", "class");
                        }}
                        }}
                       
                    }} catch (e) {{
                        send({{
                            type: 'error',
                            extra: "hook all methods error",
                            package_name: "{package_name}",
                            class_name: "{cls}",
                            error: "" + e
                        }});
                    }}
                    """

    overload += """
    });
    """
    return overload


def start_app(package_name):
    try:
        print(f'start {package_name}')
        device = frida.get_usb_device()
        print(package_name)
        print(device)
        pid = device.spawn([package_name])
        session = device.attach(pid)
        script = session.create_script(get_script_code(package_name))
        # with open("script.txt", "a") as file:
        #     file.write(get_script_code(package_name))
        script.on('message', on_message)
        script.load()
        device.resume(pid)
        time.sleep(30)
        session.detach()
    except Exception as e:
        log_error("Running Error", f"pkg:{package_name}, {str(e)}")


# test_script = """
#      Java.perform(function () {{
#          Java.deoptimizeEverything()
#          let AppLovinPrivacySettings = Java.use("com.applovin.sdk.AppLovinPrivacySettings");
#          AppLovinPrivacySettings["setDoNotSell"].overload('boolean', 'android.content.Context').implementation = function (z, context) {{
#              console.log("enter");
#              console.log("AppLovinPrivacySettings.setDoNotSell is called: z=" + z + ", context=" + context);
#              this.setDoNotSell(z, context);
#          }};
#
#         }});
# """

def run_monkey_taps(package_name):
    # Simulate taps using Monkey
    subprocess.run(['adb', 'shell', 'monkey', '-p', package_name, '--throttle', '10', '100'])

def isPricacyAPI(cls, mtd):
    apis = loadAllMethods()
    for api in apis:
        if api["Class"] == cls and api["API"] == mtd:
            return True
    return False

def on_message(message, data):
    if 'payload' in message:
        payload = message['payload']
        type = payload.get('type')
        pkg = payload.get('package_name')

        if type == 'log':
            payload["is_privacy"] = isPricacyAPI(payload.get('class_name'), payload.get('method'))
            formatted_payload = json.dumps(payload, indent=4)
            print(formatted_payload)
            with open(f"log/apk_log/{pkg}.log", "a") as file:
                file.write(formatted_payload + ",\n")
        elif type == "error":
            formatted_payload = json.dumps(payload, indent=4)
            with open(f"log/apk_error/{pkg}.log", "a") as file:
                file.write(formatted_payload + ",\n")


def loadAllMethods():
    with open("data/apis.json", "r") as file:
        data = json.loads(file.read())
    return data

def clickContinue():
    result = subprocess.run(['adb', 'shell', 'input', 'tap', '273', '2092'], capture_output=True, text=True)
    time.sleep(2)
    result3 = subprocess.run(['adb', 'shell', 'input', 'tap', '316', '2242'], capture_output=True, text=True)

    # Print output and error
    print("stdout:", result.stdout)
    print("stderr:", result.stderr)

def loadAllClasses():
    with open("data/classes.json", "r") as file:
        data = json.loads(file.read())
    return data


def installApk(device_file_path, path, pkg_name, file_path):
    global install_failed

    install_failed = False
    try:
        if filename.lower().endswith(".apk"):
            result = subprocess.run(['adb', 'shell', 'pm', 'install', '-t', '-r', device_file_path])
            if result.returncode != 0:
                install_failed =True
        else:
            # try multiple install
            xapk_path = os.path.join(f"{path}/apk_extract", pkg_name)
            apk_files = extract_xapk(file_path, xapk_path)
            apk_files = [file for file in apk_files if file.endswith('.apk')]
            apk_paths = [f"{xapk_path}/{file}" for file in apk_files]
            command = ["adb", "install-multiple"]
            command += apk_paths
            result = subprocess.run(command)
            if result.returncode != 0:
                install_failed = True
    except Exception as e:
        try:
            log_error("Install Error", f"pck:{pkg_name}  error:{str(e)}")
            install_failed = True
        except Exception as e:
            print(f"error: {str(e)}")



device_path = "/data/local/tmp/"
path_list = ["/Volumes/YorcaDisk/class_apks"]#["/Volumes/Yorca_T7/apks_new"]  ["/Volumes/YorcaDisk/class_apks"]   ["/Users/yorca/projects/sdk_interaction/testing_app/APKs"]
if not os.path.exists("executed_apks.log"):
    with open("executed_apks.log", "a") as file:
        file.write(f"")
for path in path_list:
    try:
        for filename in os.listdir(path):
            if filename == "app-debug.apk":
                continue
            if not filename.lower().endswith(".xapk") and not filename.lower().endswith(".apk"):
                continue
            file_path = os.path.join(path, filename)
            with open("executed_apks.log", "r") as file:
                lines = file.read().split("\n")
            if file_path in lines:
                continue
            with open("executed_apks.log", "a") as file:
                file.write(f"{file_path}\n")
            pkg_name = ""
            if "---" in filename:
                pkg_name = filename.split("---")[0]
            elif filename.endswith("apk"):
                pkg_name = get_apk_package_name(file_path)
            else:
                xapk_path = os.path.join(f"{path}/apk_extract0", pkg_name)
                apk_files = extract_xapk(file_path, xapk_path)
                for apkfile in extract_xapk(file):
                    extracted_name = get_apk_package_name(apkfile)
                    if extracted_name != None:
                        pkg_name = extracted_name
            if not pkg_name:
                continue
            subprocess.run(['adb', 'push', file_path, device_path])

            print(f"start install {file_path}")
            device_file_path = f'{device_path}{filename}'

            th1 = threading.Thread(target=installApk, args=(device_file_path, path, pkg_name, file_path))
            th2 = threading.Thread(target=click_pop_window_by_xml, args=(['继续安装', '完成'],))

            th1.start()
            th2.start()

            th1.join()
            th2.join()

            if not install_failed:
                start_app(pkg_name)
                subprocess.run(['adb', 'uninstall', pkg_name])
                subprocess.run(['adb', 'shell', 'rm', device_file_path])
                print(f'APK {filename} processed. Package name: {pkg_name}')

    except:
        pass