from netmiko import ConnectHandler
import os
from dotenv import load_dotenv

load_dotenv()

def get_show_version():
    device = {
        "device_type": "cisco_ios",
        "host": os.environ.get("DEVICE_HOST"),
        "username": os.environ.get("DEVICE_USERNAME"),
        "password": os.environ.get("DEVICE_PASSWORD"),
    }

    try:
        connection = ConnectHandler(**device)
        output = connection.send_command("show version")
        connection.disconnect()
        return output
    except Exception as e:
        return f"Connection failed: {e}"
