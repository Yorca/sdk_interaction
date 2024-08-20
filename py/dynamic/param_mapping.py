import frida
import subprocess
import time

# script = f"""
#     Java.perform(function () {{
#         cls_name = ""
#         var clazz = Java.use(cls_name)
#         if (!clazz) {{
#             return
#         }}
#         var overloadCount = clazz[methodName]?.overloads?.length
#         if (!overloadCount || overloadCount <= 0) {{
#             return
#         }}
#
#         for (var i = 0; i < overloadCount; i++) {{
#             (function () {{
#                 var originalMethod = clazz[methodName].overloads[i]
#
#                 var result = originalMethod.apply(this, arguments);
#                 originalMethod.implementation = function () {{
#                     send({{
#                         type: 'log',
#                         method: methodName,
#                         package_name:pkg,
#                         class_name:cls_name,
#                         timestamp: new Date().getTime(),
#                         ref: this + '',
#                         arguments: JSON.stringify(arguments),
#                         stack_trace: Java.use('android.util.Log').getStackTraceString(Java.use('java.lang.Exception').$new())
#                     }});
#
#
#
#
#
#                    return result;
#                    }};
#                }})();
#         }}
#
#
#     }}
#
#
# """


script = f"""
    Java.perform(function () {{
        let AppLovinPrivacySettings = Java.use("com.applovin.sdk.AppLovinPrivacySettings");
        AppLovinPrivacySettings["setIsAgeRestrictedUser"].implementation = function (z, context) {{
            console.log(`AppLovinPrivacySettings.setIsAgeRestrictedUser is called: z=${{z}}, context=${{context}}`);
            this["setIsAgeRestrictedUser"](z, context);
        }}
}}
"""

def on_message(message, data):
    if 'payload' in message:
        payload = message['payload']
        print(payload)
        # formatted_payload = json.dumps(payload, indent=4)
        # type = payload.get('type')
        # if type == 'log':
        #     print("message:" + str(message))
        #     print("data:" + str(data))
        # txt_file_name = f'output_{type}.txt'
        # if not os.path.exists(txt_file_name):
        #     with open(txt_file_name, 'w'):
        #         pass
        #
        # with open(txt_file_name, 'a') as txt_file:
        #     txt_file.write(formatted_payload + '\n')

device = frida.get_usb_device()
pid = device.spawn(["com.sdkint.sdkintapplovinfacebook"])
session = device.attach(pid)
script = session.create_script(script)
script.on('message', on_message)
script.load()
device.resume(pid)
time.sleep(30)
session.detach()


