import os
from ciscotool.show_version import get_show_version

device_hosts = os.environ.get("DEVICE_HOSTS", "").split(",")

for host in device_hosts:
    host = host.strip()
    if not host:
        continue
    print(f"\n--- Connecting to {host} ---")
    os.environ["DEVICE_HOST"] = host
    output = get_show_version()
    print(output)

