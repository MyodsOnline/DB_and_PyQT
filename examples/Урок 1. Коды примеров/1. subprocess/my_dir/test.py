import platform
import os
import ipaddress

os_name_ = platform.system()

os_name = os.name

ipv4 = ipaddress.ip_address('127.0.0.1')

if ipv4.is_loopback:
    print(dir(ipv4))
else:
    pass
