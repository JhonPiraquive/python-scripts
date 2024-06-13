from Crypto.PublicKey import RSA

def extract_n_from_pubkey(pubkey_path):
    with open(pubkey_path, 'r') as file:
        key_content = file.read()

    # Crear la clave pública a partir del contenido del archivo
    rsa_key = RSA.import_key(key_content)

    # Obtener el módulo 'n'
    return rsa_key.n

# Ruta al archivo .pub
pubkey_path = './id_rsa.pub'

try:
    n = extract_n_from_pubkey(pubkey_path)
    print(f"El valor de n es: {n}")
except Exception as e:
    print(f"Error: {e}")