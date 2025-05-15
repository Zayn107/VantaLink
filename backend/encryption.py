from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_message(key, message):
    return Fernet(key).encrypt(message.encode())

def decrypt_message(key, token):
    return Fernet(key).decrypt(token).decode()