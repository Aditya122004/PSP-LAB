encrypt = lambda text, shift: ''.join(chr(ord(ch) + shift) for ch in text)
decrypt = lambda text, shift: ''.join(chr(ord(ch) - shift) for ch in text)

text = input("Enter text: ")
shift = int(input("Enter shift number: "))

encrypted_text = encrypt(text, shift)
print("\nEncrypted text:", encrypted_text)

input("\nPress Enter to show decrypted text...")

decrypted_text = decrypt(encrypted_text, shift)
print("Decrypted text:", decrypted_text)
