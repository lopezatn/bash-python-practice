import os, socket

current_directory = os.getcwd()
current_user = os.getenv("USER")
host_name = socket.gethostname()


print(f"Current directory: {current_directory}")
print(f"Current User: {current_user}")
print(f"Hostname: {host_name}")

for file in os.listdir("."):
    if file.endswith(".sh"):
        print(f"File name: {file}")

