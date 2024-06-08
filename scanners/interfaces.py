import psutil

def get_network_interfaces():
    # Obtiene las interfaces de red
    interfaces = psutil.net_if_addrs()

    # Imprime las interfaces de red y sus direcciones
    for interfaz, direcciones in interfaces.items():

        print(f"Interfaz: {interfaz}")

        for direccion in direcciones:
            # Verifica el tipo de dirección y muestra la dirección
            if str(direccion.family) == 'AddressFamily.AF_INET':
                print(f"  IPv4: {direccion.address}")
            elif str(direccion.family) == 'AddressFamily.AF_INET6':
                print(f"  IPv6: {direccion.address}")
