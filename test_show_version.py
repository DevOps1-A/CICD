from ciscotool import show_version
from unittest.mock import patch, MagicMock

def test_get_show_version():
    mock_output = "Cisco IOS Software, C2960 Software (C2960-LANBASEK9-M)"

    # Correct patch path: patch where it's imported, not where it's used
    with patch("ciscotool.ConnectHandler") as mock_connect:
        mock_conn = MagicMock()
        mock_conn.send_command.return_value = mock_output
        mock_conn.disconnect.return_value = None
        mock_connect.return_value = mock_conn

        result = show_version.get_show_version()
        assert "Cisco IOS" in result
