import socket
import pytest
from driver import Driver


def test_driver_integrated():
    d = Driver(socket.gethostname())
    result = d.disk_free()
    percent = d.extract_percent(result)
    assert percent == "75%"


def test_driver_unit(mocker):
    output_list = [
        "Filesystem      Size  Used Avail Use% Mounted on",
        "rootfs          472G  128G  344G  28% /",
        "none            472G  128G  344G  28% /dev",
    ]
    output = "\n".join(output_list)
    mock_run = mocker.patch(
        "driver.Driver.run", return_value=output
    )
    d = Driver(socket.gethostname())
    result = d.disk_free()
    # free_line = result.split("\n")[1]
    # percent = free_line.split()[4]
    percent = d.extract_percent(result)
    mock_run.assert_called_with("df -h")
    assert percent == "28%"
