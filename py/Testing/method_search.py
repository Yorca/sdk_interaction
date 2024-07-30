from androguard.misc import AnalyzeAPK

# Path to the APK file
apk_path = "/Users/yorca/Downloads/Braindom_BrainGamesTest_2.3.2_Apkpure.apk"
# Keywords to search for in method names
keywords = ["gdpr", "ccpa"]


def find_methods_with_keywords(apk_path, keywords):
    # Analyze the APK
    a, d, dx = AnalyzeAPK(apk_path)

    # Store methods containing keywords
    methods_with_keywords = []

    # Iterate over all classes
    for class_analysis in dx.get_classes():
        # Iterate over all methods in the class
        for method_analysis in class_analysis.get_methods():
            method = method_analysis.get_method()
            # Construct full method name including class and parameters
            full_method_name = "{}->{}{}".format(method.class_name, method.name, method.descriptor)
            # Check if any keyword is in the full method name
            if any(keyword in full_method_name for keyword in keywords):
                # Add the method if it contains a keyword
                methods_with_keywords.append(full_method_name)

    return methods_with_keywords


# Example usage
methods = find_methods_with_keywords(apk_path, keywords)
for method in methods:
    print(method)