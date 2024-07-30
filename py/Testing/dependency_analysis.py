from androguard.misc import AnalyzeAPK
import androguard.core.analysis.analysis
import pickle

def find_method_usage(apk_path, class_name, method_name):
    a, d, dx = AnalyzeAPK(apk_path)
    # with open('apk_a.pkl', 'wb') as f:
    #     pickle.dump(a, f)
    # with open('apk_d.pkl', 'wb') as f:
    #     pickle.dump(d, f)
    # with open('apk_dx.pkl', 'wb') as f:
    #     pickle.dump(dx, f)

    target_class = class_name.replace('.', '/')
    print(target_class)
    target_method = method_name
    for method in dx.find_methods(classname=target_class, methodname=target_method):
        print(f"Found method: {method.name}, in class: {method.class_name}")
        # for _, call, _ in method.get_xref_from():
        #     print(f" - Called from method: {call.name}, in class: {call.class_name}")


apk_path = "/Users/yorca/Downloads/KawaiiWorld-CraftandBuild_1.5.2_Apkpure.apk"
class_name = "Lio/bidmachine/BidMachine;"
api_name = "setCoppa"
find_method_usage(apk_path, class_name, api_name)