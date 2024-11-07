# import subprocess
#
# command = [
#     "adb", "shell",
#     "CLASSPATH=/sdcard/monkeyq.jar:/sdcard/framework.jar:/sdcard/fastbot-thirdpart.jar",
#     "exec", "app_process", "/system/bin",
#     "com.android.commands.monkey.Monkey",
#     "-p", "com.xingin.xhs",
#     "--agent", "reuseq",
#     "--running-minutes", "1",
#     "--throttle", "500",
#     "-v", "-v",
#     "--output-directory", "/sdcard/fastbot_log"
# ]
# with open("fastbot_output.log", "w") as file:
#     process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#
#     # Write stdout to file and console
#     for line in process.stdout:
#         print(line, end='')  # Print to console
#         file.write(line)     # Write to file
#
#     # Write stderr to file and console
#     for line in process.stderr:
#         print(line, end='')  # Print to console
#         file.write(line)     # Write to file
#
# # Wait for the process to complete
#     process.wait()
#