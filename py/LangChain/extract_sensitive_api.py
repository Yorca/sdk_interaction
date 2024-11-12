import re
import json

# Define translation dictionary
translations = {
    '获取IMEI': 'Retrieve IMEI',
    '获取MEID': 'Retrieve MEID',
    '获取电话号码标识符': 'Retrieve phone number identifier',
    '获取IMSI/iccid': 'Retrieve IMSI/ICCID',
    '获取IMSI': 'Retrieve IMSI',
    '获取MCC/MNC': 'Retrieve MCC/MNC',
    '获取SIM卡国家代码': 'Retrieve SIM card country code',
    '获取电话当前位置信息': 'Retrieve current phone location',
    '获取基站信息': 'Retrieve base station information',
    '获取sim卡是否可用': 'Retrieve SIM card availability',
    '申请具体权限看"参数1"': 'Request specific permission (see "Parameter 1")',
    '获取基站cid信息': 'Retrieve base station CID information',
    '获取基站lac信息': 'Retrieve base station LAC information',
    '获取短信信息-发送短信': 'Retrieve SMS information - send SMS',
    '获取安卓ID': 'Retrieve Android ID',
    '获取设备序列号': 'Retrieve device serial number',
    '获取mac地址': 'Retrieve MAC address',
    '读取剪切板信息': 'Read clipboard information',
    '写入剪切板信息': 'Write clipboard information',
    '读取手机IccId信息': 'Read phone IccId information',
    '读取小米手机UDID': 'Read Xiaomi phone UDID',
    '读取小米手机OAID': 'Read Xiaomi phone OAID',
    '读取小米手机VAID': 'Read Xiaomi phone VAID',
    '读取小米手机AAID': 'Read Xiaomi phone AAID',
    '读取三星手机OAID': 'Read Samsung phone OAID',
    '读取三星手机VAID': 'Read Samsung phone VAID',
    '读取三星手机AAID': 'Read Samsung phone AAID',
    'APP获取了其他app信息': 'App retrieved other app information',
    '获取了正在运行的App': 'Retrieved running app information',
    '获取了正在运行的服务面板': 'Retrieved running service panel',
    '获取wifi SSID': 'Retrieve WiFi SSID',
    '获取wifi BSSID': 'Retrieve WiFi BSSID',
    '获取wifi信息': 'Retrieve WiFi information',
    '获取wifi状态信息': 'Retrieve WiFi status information',
    '获取网络类型': 'Retrieve network type',
    '获取网络类型名称': 'Retrieve network type name',
    '获取网络名称': 'Retrieve network name',
    '获取网络是否可用': 'Retrieve network availability',
    '获取网络是否连接': 'Retrieve network connection status',
    '获取网络状态信息': 'Retrieve network status information',
    '获取Mac地址': 'Retrieve MAC address',
    '获取网络hostaddress信息': 'Retrieve network host address information',
    '获取网络address信息': 'Retrieve network address information',
    '获取网络hostname信息': 'Retrieve network hostname information',
    '调用摄像头拍照': 'Invoke camera to take picture',
    '调用摄像头': 'Invoke camera',
    '获取麦克风': 'Retrieve microphone',
    '获取传感器信息': 'Retrieve sensor information',
    '获取IP地址': 'Retrieve IP address',
    '文件操作': 'File operation'
}

# Load the JavaScript file content
with open("script.js", "r", encoding="utf-8") as file:
    js_code = file.read()

# Regex patterns to extract class name, method data, and actions
class_pattern = re.compile(r"hook\('([^']+)'")
method_pattern = re.compile(r"\{'methodName':\s*'([^']+)',\s*'action':\s*([^,]+),\s*'messages':\s*'([^']+)'\}")

# Finding all hook classes and corresponding methods
hooks = []
for match in class_pattern.finditer(js_code):
    class_name = match.group(1)
    action_match = re.search(r"var action = '([^']+)'", js_code[:match.start()])
    action = action_match.group(1) if action_match else ""

    # Extract methods within the hook
    method_data = method_pattern.findall(js_code[match.end():])
    for method_name, action_var, message in method_data:
        action_value = action if action_var == "action" else action_var
        translated_message = translations.get(message, message)  # Translate if available
        hooks.append({
            "class_name": class_name,
            "method_name": method_name,
            "action": action_value,
            "messages": translated_message
        })

# Output the extracted and translated information as JSON
with open("res/sensitive_apis.json", "a") as file:
    file.write(json.dumps(hooks, indent=4, ensure_ascii=False))

