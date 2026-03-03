import sys, subprocess

service = sys.argv[1]

try:
    service_status = subprocess.run(["systemctl", "is-active", service], capture_output=True, text=True)
    result = service_status.stdout.strip()

    if result == "active":
        print(f"{service} is running")
    else:
        print(f"{service} is NOT running")
except subprocess.CalledProcessError:
    print("subprocess.check_output FAILED")

