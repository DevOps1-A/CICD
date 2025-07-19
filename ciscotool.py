from netmiko import ConnectHandler

def get_show_version(device_params):
    with ConnectHandler(**device_params) as net_connect:
        return net_connect.send_command("show version")
