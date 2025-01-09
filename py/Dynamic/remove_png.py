import os

for folder in os.listdir('res/fastbot_log/'):
    path = os.path.join('res/fastbot_log/', folder, folder)
    if not os.path.exists(path):
        continue
    for filename in os.listdir(path):
        if filename.endswith('.png') and not filename.startswith("."):
            os.remove(os.path.join(path, filename))
            print(os.path.join(path, filename))