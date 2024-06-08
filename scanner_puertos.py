#Escaner de puertos y vulnerabilidades (Basico)
import socket

def scan_ports(target_ip, start_port, end_port):
    """
    Escáner de puertos básico que verifica si un rango de puertos está abierto en una dirección IP específica.

    Argumentos:
        target_ip (str): La dirección IP del objetivo.
        start_port (int): El puerto inicial para escanear.
        end_port (int): El puerto final para escanear.
    """

    for port in range(start_port, end_port + 1):
        try:
            # Crea un socket de red IPv4 y TCP.
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Establece un tiempo de espera de 0.5 segundos para las operaciones de socket.
            sock.settimeout(0.5)

            # Intenta establecer una conexión TCP con el host en el puerto especificado.
            sock.connect((target_ip, port))

            # Si la conexión se establece correctamente, imprime un mensaje indicando que el puerto está abierto.
            print(f"Puerto {port} abierto")

            # Cierra el socket después de la conexión.
            sock.close()
        except Exception as e:
            # Pasa (no hace nada) si ocurre una excepción durante la conexión.
            pass


if __name__ == "__main__":
    # Define la dirección IP objetivo a escanear. Cambia "127.0.0.1" por la dirección IP que deseas escanear.
    target_ip = "127.0.0.1"

    # Define el puerto inicial del rango a escanear.
    start_port = 80

    # Define el puerto final del rango a escanear.
    end_port = 443

    # Llama a la función scan_ports para escanear el rango de puertos especificado.
    scan_ports(target_ip, start_port, end_port)