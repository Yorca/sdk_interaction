import frida
import subprocess
import time



# frida_script = f"""
#     Java.perform(function () {{
#         let AppLovinPrivacySettings = Java.use("com.applovin.sdk.AppLovinPrivacySettings");
#         console.log(AppLovinPrivacySettings["setIsAgeRestrictedUser"].overloads);
#         AppLovinPrivacySettings["setIsAgeRestrictedUser"].overload('boolean', 'android.content.Context').implementation = function (z, context) {{
#             console.log("enter");
#             console.log("AppLovinPrivacySettings.setIsAgeRestrictedUser is called: z=" + z + ", context=" + context);
#             this.setIsAgeRestrictedUser(z, context);
#         }};
#
#         let AdSettings = Java.use("com.facebook.ads.AdSettings");
#         console.log(AdSettings["setMixedAudience"].overloads[0]);
#         AdSettings["setMixedAudience"].overload[0].implementation = function (mixedAudience) {{
#             console.log("enter");
#
#             this["setMixedAudience"](mixedAudience);;
#         }};
#     }});
# """


frida_script = f"""
    Java.perform(function () {{
        Java.deoptimizeEverything()
        let AppLovinPrivacySettings = Java.use("com.applovin.sdk.AppLovinPrivacySettings");
        AppLovinPrivacySettings["setIsAgeRestrictedUser"].implementation = function (z, context) {{
            console.log("z = " + z);
            console.log("setIsAgeResctictedUser to false");
            this["setIsAgeRestrictedUser"](false, context);
        }};
        
        let AdSettings = Java.use("com.facebook.ads.AdSettings");
        AdSettings["setMixedAudience"].implementation = function (mixedAudience) {{
            console.log("setMixedAudience is " + mixedAudience);
            this["setMixedAudience"](mixedAudience);
        }};
    }});
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
pid = device.spawn(["com.sdkint.applovinfacebook2"])
session = device.attach(pid)
print(frida_script)
script = session.create_script(frida_script)
script.on('message', on_message)
script.load()
device.resume(pid)
time.sleep(30)
session.detach()


