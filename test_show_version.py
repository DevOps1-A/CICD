from ciscotool import get_show_version
from unittest.mock import patch, MagicMock

def test_get_show_version():
    mock_output = "Cisco IOS Software, C2960 Software (C2960-LANBASEK9-M)"
    device_params = {
        "device_type": "cisco_ios",
        "host": "1.2.3.4",
        "username": "user",
        "password": "pass",
    }

    with patch("ciscotool.ConnectHandler") as mock_connect:
        mock_conn = MagicMock()
        # Mock send_command() to return mock_output
        mock_conn.send_command.return_value = mock_output
        # Make the ConnectHandler() mock support the context manager
        mock_connect.return_value.__enter__.return_value = mock_conn

        result = get_show_version(device_params)
        assert "Cisco IOS" in result
