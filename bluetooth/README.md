This script allows the Raspberry Pi to run as an RFCOMM bluetooth server. run as sudo.


# Getting started
apend to /lib/systemd/system/bluetooth.service to run daemon in compatibility mode:
    ExecStart=/usr/lib/bluetooth/bluetoothd -C
install dependencies: pybluez
append to /etc/bluetooth/main.conf: DisablePlugins = pnat

sudo python rfcomm-server.py


Raspberry Pi should now be discoverable so that users can pair from their android device by connecting to 'Pet Box'
