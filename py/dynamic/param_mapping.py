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
        var testClass2 = Java.use("com.sdkint.applovinfacebook2.testClass2");
        console.log(testClass2.testFrida);
        testClass2.testFrida.overload().implementation = function () {{
            console.log("test");
            testClass2.testFrida.call(this);
        }};
    }});
"""


# let AdSettings = Java.use("com.facebook.ads.AdSettings");
# AdSettings["setMixedAudience"].implementation = function (mixedAudience) {
#     console.log(`AdSettings.setMixedAudience is called: mixedAudience=${mixedAudience}`);
#     this["setMixedAudience"](mixedAudience);
# };



# frida_script = f"""
#     Java.perform(function () {{
#         (function() {{
#         let AppLovinPrivacySettings = Java.use("com.applovin.sdk.AppLovinPrivacySettings");
#         var originalMethod = AppLovinPrivacySettings["setIsAgeRestrictedUser"].overloads[0];
#         originalMethod.implementation = function () {{
#             console.log("enter")
#             send({{
#                 type: 'log'}});
#             var result = originalMethod.apply(this, arguments);
#             return result;}};
# }})();
#     }});
# """

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


