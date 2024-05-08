from androguard.misc import AnalyzeAPK

apk_path = '/Users/yorca/Downloads/Braindom_BrainGamesTest_2.3.2_Apkpure.apk'
a, d, dx = AnalyzeAPK(apk_path)

# Example: Accessing a specific class and method
for method in dx.find_methods(classname='Ladmost/sdk/base/AdMostConfiguration;', methodname='showPersonalizedAdForGDPR'):
    print(method)
