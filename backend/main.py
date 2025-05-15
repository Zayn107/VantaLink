import os
from encryption import generate_key, encrypt_message, decrypt_message

key = generate_key()

print("Welcome to VantaLink (Core Loop)")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("Stares > ")
    if user_input.lower() == "exit":
        break
    encrypted = encrypt_message(key, user_input)
    decrypted = decrypt_message(key, encrypted)
    print(f"Noir > I received: '{decrypted}' (encrypted in transit)\n")
