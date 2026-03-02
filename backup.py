import os, sys, shutil

file_name = sys.argv[1]
file_exists = os.path.exists(file_name)

if file_exists:
    shutil.copy(file_name, file_name + ".bak")
    print(f"Backup created: {file_name + ".bak"}")
else:
    print("Error, file not found")
