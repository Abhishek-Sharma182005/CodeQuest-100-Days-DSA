text=input("Enter cipher text:")
n=int(input("Enter shift value:"))
decoded_message=" "
for char in text:
    if char.isalpha():
        base = ord('A') if char.isupper() else ord('a')
        decoded_char = chr((ord(char) - base - n) % 26 + base)
        decoded_message += decoded_char
    else:
        decoded_message += char

print("Decoded message:", decoded_message)