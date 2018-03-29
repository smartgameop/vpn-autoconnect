__author__ = "Optimus Prime"
__copyright__ = "Copyright 2018, The Prime Lab inc"
__credits__ = ["Optimus Prime"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Optimus Prime"
__status__ = "Testing"
__date__ = "29/03/18"

import os
import subprocess
import logging
import time
import netifaces

logging.basicConfig(filename='auto_vpn.log', level=logging.DEBUG)


def check_ping():
    hostname = "google.com"
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        ping_status = "Network_Active"
        print(ping_status)
        current_list = netifaces.interfaces()
        if "lo" in current_list:
            pass
        else:
            subprocess.call("ifconfig enp1s0 down", shell=True)
            subprocess.call("pkill -9 openvpn", shell=True)
            subprocess.call("openvpn --config client.ovpn >/dev.null &", shell=True)
            time.sleep(15)
            subprocess.call("ifconfig enp1s0 up", shell=True)

    else:
        ping_status = "Network_Error"
        print(ping_status)
        subprocess.call("ifconfig enp1s0 down", shell=True)
        subprocess.call("pkill -9 openvpn", shell=True)
        subprocess.call("openvpn --config client.ovpn >/dev/null &", shell=True)
        time.sleep(15)
        subprocess.call("ifconfig enp1s0 up", shell=True)


while True:
    check_ping()
    time.sleep(6)
