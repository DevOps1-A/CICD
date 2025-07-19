import os
from ciscotool import get_show_version  # ✅ Correct way for a single-file module

device_hosts = os.environ.get("DEVICE_HOSTS", "").split(",")

for host in device_hosts:
    host = host.strip()
    if not host:
        continue
    print(f"\n--- Connecting to {host} ---")
    os.environ["DEVICE_HOST"] = host
    # You likely want to pass device_params here:
    device_params = {
        "device_type": "cisco_ios",
        "host": host,
        "username": os.environ.get("DEVICE_USERNAME"),
        "password": os.environ.get("DEVICE_PASSWORD"),
    }
    output = get_show_version(device_params)
    print(output)
