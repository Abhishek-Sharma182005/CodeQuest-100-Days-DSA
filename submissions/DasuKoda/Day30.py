def decode(text,shift):
    decoded=""
    for char in text:
        if char.isalpha():
            base=ord('A') if char.isupper() else ord('a')
            decoded+=chr((ord(char) -base-shift) % 26 + base)
        else:
            decoded+=char
    print("decoded : ",decoded)


decode("Khoor Zruog", 3)

"""
output

decoded :  Hello World
"""
