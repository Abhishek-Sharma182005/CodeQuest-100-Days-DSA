packet = input("Enter packet data: ")

ascii_sum = 0

for char in packet:
    ascii_sum += ord(char)

checksum = ascii_sum % 256

print("Checksum: ",checksum)