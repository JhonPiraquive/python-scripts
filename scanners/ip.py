import platform
import requests
import subprocess
from scapy.all import ARP, Ether, srp, conf

def get_ip():
    """
        IP local y publica
    
        Este comando permite obtener tanto la IP local como la pública con la que se está accediendo a la red

        Returns
        -------
        ip : (string, string)
            Una tupla con la IP local y pública
    """

    try:
        if platform.system() == 'Windows':
            local = subprocess.getoutput("""for /f "tokens=2 delims=[]" %a in ('ping -n 1 -4 "%computername%"') do @echo %a""")
        else:
            local = subprocess.getoutput("ifconfig | grep 'inet ' | grep -Fv 127.0.0.1 | awk '{print $2}'")
    except:
        public = 'unknown'
        
    try:
        public = requests.get('http://checkip.amazonaws.com').text.strip()
    except:
        public = 'unknown'
        
    print(f'Gateway IP: {local}')
    print(f'Public IP: {public}')

    return (local, public)

def scan_ips(network, interface):
    conf.iface = interface

    # Crea un paquete ARP para la red especificada
    arp = ARP(pdst=network)

    # Crea un paquete de tramas Ethernet para la solicitud ARP
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")

    # Combina ambos paquetes
    packet = ether/arp
    
    print(arp, ether, packet)

    # Envía el paquete y recibe las respuestas
    result = srp(packet, timeout=3, verbose=0)[0]
    
    # Extrae las direcciones IP de las respuestas
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    
    print('devices')
    print(devices)

    for device in devices:
        print(f"IP Address: {device['ip']}, MAC Address: {device['mac']}")

    return devices
