from cryptography.fernet import Fernet
import base64
import hashlib

def generate_key(secret_phrase):
    # Deriva una clave de la frase secreta
    key = hashlib.sha256(secret_phrase.encode()).digest()
    return base64.urlsafe_b64encode(key)

def encrypt_data(data, key):
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

if __name__ == "__main__":
    secret_phrase = "Frase que guarde esa clave"  
    key = generate_key(secret_phrase)

    # Encriptar la clave y guardarla
    encrypted_key = encrypt_data("Texto o clave que quieras encriptar", key) 

    with open("mi_clave_encriptada.key", "wb") as key_file:
        key_file.write(encrypted_key)
    print(f"Clave encriptada guardada: {encrypted_key}")
