from androguard.misc import AnalyzeAPK
import networkx as nx
import matplotlib.pyplot as plt

def analyze_apk(apk_path, class_name, api_name):
    a, d, dx = AnalyzeAPK(apk_path)

    # Find the class and method of interest
    class_analysis = dx.find_classes(class_name)
    for method in dx.find_methods(classname=class_name, methodname=api_name):
        method_analysis = method.get_method()

        # Print all API calls made by this method
        for _, call, _ in method_analysis.get_xref_to():
            print(f"API called: {call.class_name}.{call.name}")

        # Here you'd build your graph based on the API calls
        # For simplicity, this step is not implemented

def visualize_graph(G):
    plt.figure(figsize=(10, 8))
    nx.draw(G, with_labels=True, node_color='skyblue', arrowstyle='->', arrowsize=10,
            font_size=8, font_weight='bold', node_size=2000, pos=nx.spring_layout(G))
    plt.title('API Dependency Graph')
    plt.show()

# Example usage
apk_path = '/Users/yorca/Downloads/Braindom_BrainGamesTest_2.3.2_Apkpure.apk'
class_name = 'admost.sdk.base.AdMostConfiguration'
method_name = 'showPersonalizedAdForGDPR'
analyze_apk(apk_path, class_name, method_name)
