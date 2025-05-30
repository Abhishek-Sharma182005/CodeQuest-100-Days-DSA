numbers = input("Enter numbers: ").split()
decoder_message = ''.join(chr(int(num))for num in numbers)
print("Decoded Message:",decoder_message)