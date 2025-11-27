# Caesar Cipher Implementation

def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        if char.isalpha():  # check if alphabet
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                result += chr((ord(char) - base + shift) % 26 + base)
            elif mode == 'decrypt':
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char  # keep non-alphabet same
    return result


# ---- Main Program ----
print("=== Caesar Cipher Program ===")

message = input("Enter your message: ")
shift = int(input("Enter shift value (e.g. 3): "))
mode = input("Do you want to 'encrypt' or 'decrypt'? ").lower()

output = caesar_cipher(message, shift, mode)
print(f"\nYour {mode}ed text is: {output}")
