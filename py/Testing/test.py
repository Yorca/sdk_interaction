from androguard.misc import AnalyzeAPK


def get_method_code(apk_path, class_name, method_name):
    # 读取并解析APK文件
    a, d, dx = AnalyzeAPK(apk_path)

    # 遍历所有类
    for item in d:
        for cls in item.get_classes():
            if class_name in cls.get_name():
                # 遍历类中的所有方法
                for method in cls.get_methods():
                    if method_name == method.get_name():
                        # 获取方法的代码
                        return method.get_source()

    return None


# 示例使用
apk_path = "/Users/yorca/Downloads/KawaiiWorld-CraftandBuild_1.5.2_Apkpure.apk"
class_name = "Lcom/applovin/sdk/AppLovinPrivacySettings;"
method_name = "setIsAgeRestrictedUser"

method_code = get_method_code(apk_path, class_name, method_name)
if method_code:
    print(f"Method {method_name} in class {class_name}:\n{method_code}")
else:
    print(f"Method {method_name} not found in class {class_name}.")
