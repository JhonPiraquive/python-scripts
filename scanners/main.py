import ip
import interfaces
import ports_and_services

"""
    @maintainer Alejandro Piraquive
    
    Requirements
    --------------------------
    1. Install Modules
        - scapy
        - requests
    2. Install Npcap
"""

if __name__ == "__main__":
    print('Available Commands:\n')
    print('1. Gateway and Public Ips: Get your gateway and public ips')
    print('2. Network Interfaces: Get the network interfaces')
    print('3. Ips: Scan a given range of ips')
    print('4. Ports and Services: Scan Ports and services for a given ip')

    command = input('\nOption: ')

    match command:
        case '1':
            ip.get_ip()
        case '2':
            interfaces.get_network_interfaces()
        case '3':
            network = input('Network (ip/netmask): \n')
            interface = input('Interface: \n')
            ip.scan_ips(network, interface)
        case '4':
            target_ip = input('Target IP: \n')
            start_port = int(input('Start Port: \n'))
            end_port = int(input('End Port: \n'))
            ports_and_services.scan(target_ip, start_port, end_port)
        case _:
            print('Command not supported.')
