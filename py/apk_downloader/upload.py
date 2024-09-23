import paramiko

# Server details
hostname = 'brooks.cs.ucf.edu'
username = 'zh844971'  # Your username
password = '!Qwert825215'  # Your password (if using password authentication)
# Alternatively, use key_filename for SSH key authentication, e.g., key_filename='/path/to/your/private/key'

# File details
local_file_path = '/Users/yorca/projects/sdk_interaction/py/apk_downloader/apks/ac.voicenote.voicerecorder.audio---Voice Recorder_6.1_APKPure.xapk'  # The file on your local machine
remote_file_path = '/home/zh844971/sdk_interaction/apks3/ac.voicenote.voicerecorder.audio---Voice Recorder_6.1_APKPure.xapk'  # The path where the file will be saved on the server

try:
    # Create an SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the server
    ssh.connect(hostname=hostname, username=username, password=password)

    # Open an SFTP session
    sftp = ssh.open_sftp()

    # Upload the file
    sftp.put(local_file_path, remote_file_path)
    print(f'File uploaded successfully to {remote_file_path}')

    # Close the SFTP session and SSH connection
    sftp.close()
    ssh.close()

except Exception as e:
    print(f'Failed to upload file: {e}')
