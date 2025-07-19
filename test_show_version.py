from ciscotool import show_version
from unittest.mock import patch

def test_get_show_version():
    mock_output = "Cisco IOS Software, C2960 Software (C2960-LANBASEK9-M)"

    with patch("ciscotool.show_version.ConnectHandler") as mock_connect:
        mock_connect.return_value.send_command.return_value = mock_output
        mock_connect.return_value.disconnect.return_value = None

        result = show_version.get_show_version()
        assert "Cisco IOS" in result