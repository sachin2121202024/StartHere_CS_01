def encrypt(text, shift):

    result = ""
    
    # Traverse the text
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Non-alphabet characters remain unchanged
            result += char
    
    return result

def decrypt(cipher, shift):
    result = ""
    
    # Traverse the cipher text
    for i in range(len(cipher)):
        char = cipher[i]
        
        # Decrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        # Decrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            # Non-alphabet characters remain unchanged
            result += char
    
    return result

# Input

text = input("Enter the text to encrypt: ")
shift = int(input("Enter the shift value: "))

# Encryption
encrypted_text = encrypt(text, shift)
print(f"Encrypted Text: {encrypted_text}")

# Decryption
decrypted_text = decrypt(encrypted_text, shift)
print(f"Decrypted Text: {decrypted_text}")