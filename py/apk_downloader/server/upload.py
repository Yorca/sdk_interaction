import os

import paramiko

# Server details
hostname = 'brooks.cs.ucf.edu'
username = 'zh844971'
password = os.getenv('BROOK_PASSWORD')

# File details
# local_file_path = '/Users/yorca/projects/sdk_interaction/py/apk_downloader/apks/ac.voicenote.voicerecorder.audio---Voice Recorder_6.1_APKPure.xapk'  # The file on your local machine
# remote_file_path = '/home/zh844971/sdk_interaction/apks3/ac.voicenote.voicerecorder.audio---Voice Recorder_6.1_APKPure.xapk'  # The path where the file will be saved on the server
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=hostname, username=username, password=password)
sftp = ssh.open_sftp()
source_dir = "/Volumes/T7 Shield/apps"
remote_dir = "/home/zh844971/apks5000"
exist_list = sftp.listdir(remote_dir)
for filename in os.listdir(source_dir):
    if not filename.lower().endswith(".apk") and not filename.lower().endswith(".xapk"):
        continue
    if filename in exist_list:
        continue
    # if not filename == "com.opera.mini.native.apk":
    #     continue
    print(filename)
    local_file_path = os.path.join(source_dir, filename)
    remote_file_path = os.path.join(remote_dir, filename)

    with open("uploaded_apks.txt", "a") as file:
        file.write(f"{filename.split('---')[0]}\n")
    try:
        sftp.put(local_file_path, remote_file_path)
        # os.remove(local_file_path)
    except:
        with open("uploaded_failed.txt", "a") as file:
            file.write(f"{filename}\n")
        print(f"failed: {filename}")

sftp.close()
ssh.close()

# try:
#     # Create an SSH client
#     ssh = paramiko.SSHClient()
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
#     # Connect to the server
#     ssh.connect(hostname=hostname, username=username, password=password)
#
#     # Open an SFTP session
#     sftp = ssh.open_sftp()
#
#     # Upload the file
#     sftp.put(local_file_path, remote_file_path)
#     print(f'File uploaded successfully to {remote_file_path}')
#
#     # Close the SFTP session and SSH connection
#     sftp.close()
#     ssh.close()
#
# except Exception as e:
#     print(f'Failed to upload file: {e}')
