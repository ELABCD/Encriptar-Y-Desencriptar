from cryptography.fernet import Fernet
from encriptar import generate_key

def decrypt_data(encrypted_data, key):
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data).decode()
    return decrypted_data

if __name__ == "__main__":
    secret_phrase = "Clave_Anterior"  # Debe ser la misma frase que usaste antes
    key = generate_key(secret_phrase)

    # Leer la clave encriptada del archivo
    with open("mi_clave_encriptada.key", "rb") as key_file:
        encrypted_key = key_file.read()

    decrypted_key = decrypt_data(encrypted_key, key)
    print(f"Clave desencriptada: {decrypted_key}")
