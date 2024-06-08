#analizador de vulnerabilidades con Nmap

import nmap
import os

# Función para ejecutar el escaneo con nmap
def run_nmap_scan(target, ports):
    nm = nmap.PortScanner()
    nm.scan(target, ports)
    return nm

# Función para analizar los resultados del escaneo
def analyze_results(nm):
    vulnerabilities = []
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            for port in nm[host][proto].keys():
                if port == '80':
                    if nm[host][proto][port]['state'] == 'open':
                        if 'http' in nm[host][proto][port]['reason']:
                            vulnerabilities.append(f"Vulnerabilidad encontrada en {host}:{port} - {nm[host][proto][port]['reason']}")
    return vulnerabilities

# Función principal
def main():
    target = input("Introduce la dirección IP o el nombre de dominio del objetivo: ")
    start_port = int(input("Introduce el puerto inicial (por ejemplo, 1): "))
    end_port = int(input("Introduce el puerto final (por ejemplo, 10000): "))
    ports = f"-p{start_port}-{end_port}"
    nm = run_nmap_scan(target, ports)
    vulnerabilities = analyze_results(nm)
    if vulnerabilities:
        print("Vulnerabilidades encontradas:")
        for vulnerability in vulnerabilities:
            print(vulnerability)
    else:
        print("No se encontraron vulnerabilidades.")

if __name__ == "__main__":
    main()