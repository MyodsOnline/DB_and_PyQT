import os
import platform
from ipaddress import ip_address
from socket import gethostbyname
from subprocess import Popen, PIPE

ip_list = ['127.0.0.1', 'ya.ru', '8.8.8.8', '400.198.198.1', 'wrongg_adress.rru']


def host_ping(addresses, timeout=500, requests=1):
    print(f'Check list: {addresses}')
    if not isinstance(addresses, list):
        raise ValueError('a list of addresses must be specified!')

    results = {'Available_nods': '', 'Inaccessible_nodes': ''}

    for address in addresses:
        try:
            ip = ip_address(address)
        except ValueError:
            try:
                ip = ip_address(gethostbyname(address))
            except:
                results['Inaccessible_nodes'] = f'{str(address)}'

        proc = Popen(f'ping {ip} -w {timeout} -n {requests}', shell=False, stdout=PIPE)
        proc.wait()

        if proc.returncode == 0:
            results['Available_nods'] = f'{str(address)}\n'
            res_string = f'{address} - node is available'
        else:
            results['Inaccessible_nodes'] = f'{str(address)}\n'
            res_string = f'{address} - node is inaccessible'

        print(res_string)

    print(results)


if __name__ == '__main__':
    host_ping(ip_list)
