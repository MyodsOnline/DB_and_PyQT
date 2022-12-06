import os
import platform
from ipaddress import ip_address
from socket import gethostbyname

ip_list = ['127.0.0.1', 'ya.ru', '8.8.8.8', '400.198.198.1', 'wrongg_adress.rru']

def host_ping(addresses):
    if not isinstance(addresses, list):
        raise ValueError('a list of addresses must be specified!')

    result_list = []

    for address in addresses:
        try:
            ip = ip_address(address)
        except ValueError:
            try:
                ip = ip_address(gethostbyname(address))
            except:
                continue
        result_list.append(ip)

        print(result_list)


if __name__ == '_main__':
    host_ping(ip_list)
