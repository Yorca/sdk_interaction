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


def install_apk(apk_file):
    """Installs the APK using adb."""
    install_command = f"adb install {apk_file}"
    try:
        result = subprocess.run(install_command.split(), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(f"Failed to install APK: {e.stderr.decode()}")


def push_obb(obb_folder, package_name):
    """Pushes OBB files to the device."""
    obb_dest = f"/data/local/tmp/{package_name}"
    if os.path.exists(obb_folder):
        for root, dirs, files in os.walk(obb_folder):
            for file in files:
                obb_file = os.path.join(root, file)
                push_command = f"adb push {obb_file} {obb_dest}"
                try:
                    result = subprocess.run(push_command.split(), check=True, stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE)
                    print(f"Pushed OBB file {obb_file} to {obb_dest}")
                except subprocess.CalledProcessError as e:
                    print(f"Failed to push OBB file: {e.stderr.decode()}")
    else:
        print(f"No OBB files found in {obb_folder}")


def install_xapk(xapk_file):
    """Main function to install an XAPK file."""
    output_dir = "../extracted_xapk"
    extract_xapk(xapk_file, output_dir)

    # Look for the APK file in the extracted directory
    apk_file = None
    obb_folder = None
    for root, dirs, files in os.walk(output_dir):
        for file in files:
            if file.endswith(".apk"):
                apk_file = os.path.join(root, file)
            if 'Android/obb' in root:
                obb_folder = root

    if apk_file:
        print(f"Installing APK: {apk_file}")
        install_apk(apk_file)
    else:
        print("No APK file found in the extracted XAPK.")

    # Push OBB files if they exist
    if obb_folder:
        package_name = os.path.basename(obb_folder)  # Assuming OBB folder name is the package name
        push_obb(obb_folder, package_name)
    else:
        print("No OBB files found.")

def log_error(TAG, err):
    date_str = str(datetime.now())
    with open("../log/error.log", "a") as file:
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
                    method: methodName,
                    package_name: pkg,
                    class_name: cls_name,
                    timestamp: new Date().getTime(),
                    error: "" + e              
                }});
            }}
        }}
    """

    for hook_method in hook_methods:
        cls_name = hook_method["Class"].strip()
        mtd_name = hook_method["API"].strip()
        overload += f"""
        hookMethod("{cls_name}", "{mtd_name}", "{package_name}", "method");
        """

    for cls in class_list:
        cls = cls.strip()

        overload += f"""
                    try {{
                        var clazz = Java.use("{cls}");
                        for (var methodName in clazz) {{
                            console.log("class name = " + cls + "method name = " + methodName)
                            if (methodName === "$new") {{
                            methodName = "$init";
                            }}
                            else if (methodName.startsWith("$")) {{
                                continue;
                            }}
                            hookMethod("{cls}", methodName, "{package_name}", "class");
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
        pid = device.spawn([package_name])
        session = device.attach(pid)
        script = session.create_script(get_script_code(package_name))
        with open("script.txt", "a") as file:
            file.write(get_script_code(package_name))
        script.on('message', on_message)
        script.load()
        device.resume(pid)
        time.sleep(40)
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

def on_message(message, data):
    if 'payload' in message:
        payload = message['payload']
        formatted_payload = json.dumps(payload, indent=4)
        type = payload.get('type')
        pkg = payload.get('package_name')

        if type == 'log':
            print(formatted_payload)
            with open(f"log/apk_log/{pkg}.log", "a") as file:
                file.write(formatted_payload + ",\n")
        elif type == "error":
            with open(f"log/apk_error/{pkg}.log", "a") as file:
                file.write(formatted_payload +  ",\n")

def loadAllMethods():
    with open("../data/apis.json", "r") as file:
        data = json.loads(file.read())
    return data

def loadAllClasses():
    with open("../data/classes.json", "r") as file:
        data = json.loads(file.read())
    return data


if __name__ == '__main__':
    device_path = "/data/local/tmp/"
    path_list = ["/Volumes/YorcaDisk/class_apks"]#["/Users/yorca/projects/sdk_interaction/testing_app/APKs"]
    for path in path_list:
        try:
            for filename in os.listdir(path):
                file_path = os.path.join(path, filename)
                if not filename.endswith(".apk"):
                    continue
                # if not filename.endswith("xapk"):
                #     continue
                # xapk_path = "xapk_extract"
                # if filename.endswith("xapk"):
                #     apk_files = extract_xapk(file_path, xapk_path)
                #     apk_files = [file for file in apk_files if file.endswith('.apk')]
                #     apk_paths = [f"{xapk_path}/{file}" for file in apk_files]
                # pkg_name = filename.split("---")[0] if "---" in filename else get_apk_package_name(file_path)
                # if not pkg_name:
                #     continue
                # for apk_path in apk_paths:
                #     subprocess.run(['adb', 'push', apk_path, device_path])
                #     subprocess.run(['adb', 'shell', 'pm', 'install', '-t', '-r', device_file_path])

                pkg_name = filename.split("---")[0] if "---" in filename else get_apk_package_name(file_path)
                if not pkg_name:
                    continue
                subprocess.run(['adb', 'push', file_path, device_path])

                print(f"start install {file_path}")
                device_file_path = f'{device_path}{filename}'
                # if filename.endswith("xapk"):
                #     extract_xapk()
                result = subprocess.run(['adb', 'shell', 'pm', 'install', '-t', '-r', device_file_path])
                if result.returncode != 0:
                    log_error("Install Error", filename)
                    continue
                start_app(pkg_name)
                subprocess.run(['adb', 'uninstall', pkg_name])
                subprocess.run(['adb', 'shell', 'rm', device_file_path])
                print(f'APK {filename} processed. Package name: {pkg_name}')
        except:
            pass
