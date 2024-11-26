import os

import paramiko

# Server details
hostname = 'brooks.cs.ucf.edu'
username = 'zh844971'
password = os.getenv('BROOK_PASSWORD')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=hostname, username=username, password=password)
sftp = ssh.open_sftp()
source_dir = "/Volumes/T7 Shield/success_apks"
remote_dir = "/home/zh844971/apks5000"

for filename in sftp.listdir(remote_dir):
    if not filename.lower().endswith(".xapk") and not filename.lower().endswith(".apk"):
        continue
    print(filename)
    local_file_path = os.path.join(source_dir, filename)
    remote_file_path = os.path.join(remote_dir, filename)
    if os.path.exists(local_file_path):
        print(f"Skipping {filename}, already exists.")
        continue
    try:
        sftp.get(remote_file_path, local_file_path)
    except:
        with open("../download_failed.txt", "a") as file:
            file.write(f"{filename}\n")
        print(f"failed: {filename}")

sftp.close()
ssh.close()
