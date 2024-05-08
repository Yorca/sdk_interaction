import paramiko
import sqlite3
# SSH connection setup

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    conn = sqlite3.connect('/Users/yorca/Downloads/final_filter_all_v2.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * from sdkconnectionrough')
    apk_list = []
    call_map = {}
    for row in cursor.fetchall():
        key = row[4] + '->' + row[3]
        if key not in call_map.keys():
            apk_name = row[0].strip('.log') + '.apk'
            call_map[key] = apk_name
            apk_list.append(apk_name)
    print(call_map)


    ssh.connect('brooks.cs.ucf.edu', username='zh844971', password='!Qwert825215')

    # Use SFTP for file transfers
    with ssh.open_sftp() as sftp:
        remote_path = '/home/xu111284/yifan-24898-apps/apps'

        # List files in the remote directory
        try:
            files = sftp.listdir(remote_path)
        except Exception as e:
            print(f"Failed to list directory {remote_path}: {e}")
            files = []

        # Loop through each file and check if it contains any app name from the list
        for file in files:
            for app in apk_list:
                if app == file:
                    local_file_path = f"call_apks/{file}"  # Local path to save the file
                    remote_file_path = f"{remote_path}/{file}"

                    try:
                        sftp.get(remote_file_path, local_file_path)
                        print(f"Downloaded {file}")
                        # Break if you only want to download the first match for each app
                        break
                    except Exception as e:
                        print(f"Failed to download {file}: {e}")
                        continue

finally:
    ssh.close()
