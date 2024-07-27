def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            char_code = ord(char)
            new_code = char_code + shift_amount

            if char.islower():
                if new_code > ord('z'):
                    new_code -= 26
            elif char.isupper():
                if new_code > ord('Z'):
                    new_code -= 26

            encrypted_text += chr(new_code)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt a message: ").strip().lower()
    if choice not in ['encrypt', 'decrypt']:
        print("Invalid choice. Please type 'encrypt' or 'decrypt'.")
        return
    
    message = input("Enter your message: ").strip()
    shift = int(input("Enter the shift value: "))

    if choice == 'encrypt':
        result = encrypt(message, shift)
    else:
        result = decrypt(message, shift)

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
