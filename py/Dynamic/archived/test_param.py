import os
import subprocess
import time

import frida
import json
from datetime import datetime
import zipfile
import re

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


def get_script_code(package_name, filename):
    # hook_methods = loadAllMethods()
    class_list = ["com.lemon.lvoverseas.MainActivity"]
    print(class_list)
    overload = """
    Java.perform(function () {
        Java.deoptimizeEverything()
    
        function processArgument(arg) {
            console.log("processArgument + " +  arg)
            if (arg === null || arg === undefined) {
                return arg;
            }
    
            var JavaList = Java.use('java.util.List');
            var JavaSet = Java.use('java.util.Set');
            var JavaMap = Java.use('java.util.Maps');
        
            if (JavaList.class.isInstance(arg)) {
                var result = [];
                var iterator = arg.iterator();
                while (iterator.hasNext()) {
                    var item = iterator.next();
                    result.push(processArgument(item));
                }
                return result;
            } else if (JavaSet.class.isInstance(arg)) {
                var result = [];
                var iterator = arg.iterator();
                while (iterator.hasNext()) {
                    var item = iterator.next();
                    result.push(processArgument(item));
                }
                return result;
            } else if (JavaMap.class.isInstance(arg)) {
                console.log("JavaMap enter")
                var result = {};
                var entrySet = arg.entrySet();
                var iterator = entrySet.iterator();
                while (iterator.hasNext()) {
                    var entry = iterator.next();
                    var key = processArgument(entry.getKey());
                    var value = processArgument(entry.getValue());
                    result[key] = value;
                }
                return result;
            } else {
                try {
                    return arg.toString();
                } catch (e) {
                    return arg;
                }
            }
        }
                
    """

    overload += f"""
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
                            var argsArray = [];
                            for (var j = 0; j < arguments.length; j++) {{
                                argsArray.push(arguments[j] + "");
                            }}
                            var result = originalMethod.apply(this, arguments);
                            send({{
                                type: 'log',
                                source: source,
                                method: methodName,
                                package_name: pkg,
                                class_name: cls_name,
                                timestamp: new Date().getTime(),
                                ref: this + '',
                                return: result + "",
                                arguments: argsArray,
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

    print(overload)
    return overload


def run_fastboot(package_name):
    command = [
        "adb", "shell",
        "CLASSPATH=/sdcard/monkeyq.jar:/sdcard/framework.jar:/sdcard/fastbot-thirdpart.jar",
        "exec", "app_process", "/system/bin",
        "com.android.commands.monkey.Monkey",
        "-p", package_name,
        "--agent", "reuseq",
        "--running-minutes", "1",
        "--throttle", "500",
        "-v", "-v",
        "--output-directory", "/sdcard/fastbot_log"
    ]
    with open(f"res/UI trace/{package_name}.log", "w") as file:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        for line in process.stdout:
            file.write(line)
        for line in process.stderr:
            file.write(line)
        process.wait()

def start_app(package_name, filename):
    try:
        print(f'start {package_name}')
        device = frida.get_usb_device()
        pid = device.spawn([package_name])
        session = device.attach(pid)
        script = session.create_script(get_script_code(package_name, filename))
        script.on('message', on_message)
        script.load()
        device.resume(pid)
        print("start fastbot")
        run_fastboot(package_name)
        # time.sleep(60)
        print("end fastbot")
        session.detach()
    except Exception as e:
        print(f"error: {e}")
        log_error("Running Error", f"pkg:{package_name}, {str(e)}")

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
    with open("../data/apis.json", "r") as file:
        data = json.loads(file.read())
    return data


def loadAllClasses():
    with open("../data/classes.json", "r") as file:
        data = json.loads(file.read())
    return data

def get_classes(filename):
    with open("../data/classes_in_packages.json", "r") as file:
        data = json.loads(file.read())
    classes = data[f"{filename}.packages"]
    print(classes)
    if not classes or classes == "not found" or classes == "empty content":
        return None

    return classes.split(';')


def push_valid_string(file):
    with open("../max.valid.strings", "w") as outfile:
        subprocess.run(["aapt", "dump", "--values", "strings", file], stdout=outfile)
    subprocess.run(["adb", "push", "max.valid.strings", "/sdcard"])

def push_obb(obb_files, package_name):
    """Pushes OBB files to the device."""
    obb_destination = f"/sdcard/Android/obb/{package_name}/"
    print(f"Creating OBB directory: {obb_destination}")
    subprocess.run(["adb", "shell", "mkdir", "-p", obb_destination])
    for obb_file in obb_files:
        print(f"Pushing OBB file: {obb_file}")
        subprocess.run(["adb", "push", obb_file, obb_destination])
    print("OBB files transferred successfully.")

def installApk(device_file_path, path, pkg_name, file_path):

    try:
        if filename.lower().endswith(".apk"):
            result = subprocess.run(['adb', 'shell', 'pm', 'install', '-t', '-r', device_file_path])
            return result.returncode == 0
        else:
            # try multiple install
            xapk_path = os.path.join(f"{path}/apk_extract", pkg_name)
            apk_files = extract_xapk(file_path, xapk_path)
            apk_files = [file for file in apk_files if file.endswith('.apk')]
            obb_files = [file for file in apk_files if file.endswith('.obb')]
            apk_paths = [f"{xapk_path}/{file}" for file in apk_files]
            command = ["adb", "install-multiple"]
            command += apk_paths
            result = subprocess.run(command)
            print(f"install result = {result}")
            if result.returncode == 0:
                if obb_files:
                    push_obb(obb_files, pkg_name)
            return False
    except Exception as e:
        log_error("Install Error", f"pck:{pkg_name}  error:{str(e)}")
        return False


start_app("com.lemon.lvoverseas", "")
# device_path = "/data/local/tmp/"
# path_list = ["/Volumes/Yorca_T7/apps/8773apps"]  # ["/Volumes/Yorca_T7/apks_new"]  ["/Volumes/YorcaDisk/class_apks"]   ["/Users/yorca/projects/sdk_interaction/testing_app/APKs"]
# with open("executed_apks.log", "a") as file:
#     file.write(f"")
# for path in path_list:
#
#     for filename in os.listdir(path):
#         try:
#             print(filename)
#             if not filename.lower().endswith(".xapk") and not filename.lower().endswith(".apk"):
#                 continue
#             file_path = os.path.join(path, filename)
#             with open("executed_apks.log", "r") as file:
#                 lines = file.read().split("\n")
#             if file_path in lines:
#                 continue
#             with open("executed_apks.log", "a") as file:
#                 file.write(f"{file_path}\n")
#             pkg_name = filename.rstrip('.apk').rstrip('.xapk')
#             print("pkg:" + pkg_name)
#             if not pkg_name:
#                 continue
#             subprocess.run(['adb', 'push', file_path, device_path])
#
#             print(f"start install {file_path}")
#             device_file_path = f'{device_path}{filename}'
#
#
#             success = installApk(device_file_path,path,pkg_name, file_path)
#             if not success:
#                 continue
#
#             push_valid_string(file_path)
#
#             subprocess.run(['adb', 'uninstall', pkg_name])
#             subprocess.run(['adb', 'shell', 'rm', device_file_path])
#             os.makedirs(f"res/fastbot_log/{pkg_name}")
#             subprocess.run(['adb', 'pull', '/sdcard/fastbot_log', f"/Users/yorca/projects/sdk_interaction/py/Dynamic/res/fastbot_log/{pkg_name}"])
#             subprocess.run(['adb', 'shell', 'rm', '-rf', '/sdcard/fastbot_log'])
#             print(f'APK {filename} processed. Package name: {pkg_name}')
#
#         except Exception as e:
#             print(f"error = {e}")