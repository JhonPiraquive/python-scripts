import socket

def scan_port(target_ip, port, protocol):
    try:
        sock_type = socket.SOCK_STREAM if protocol == 'TCP' else socket.SOCK_DGRAM
        sock = socket.socket(socket.AF_INET, sock_type)
        sock.settimeout(0.5)
        sock.connect((target_ip, port))
        print(f"{port}\t\tYES\t\t{protocol}\t\t{socket.getservbyport(port)}")
    except socket.error as e:
        print(f"{port}\t\tERROR\t\t{protocol}\t\t{e}")
    finally:
        sock.close()

def scan(target_ip, start_port, end_port):
    if not start_port <= end_port:
        raise ValueError("start_port debe ser menor o igual que end_port")

    print('----- Inicio del escaneo -----')
    print('PUERTO\t\t¿ABIERTO?\t\tPROTOCOLO\t\tSERVICIO')

    for port in range(start_port, end_port + 1):
        scan_port(target_ip, port, 'TCP')
        scan_port(target_ip, port, 'UDP')

    print('---- Escaneo finalizado ----')
