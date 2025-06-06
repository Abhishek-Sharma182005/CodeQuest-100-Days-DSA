binary = input("Enter binary signal: ")
count = 0
for bit in binary:
    if bit ==1:
        count += 1
if count % 2==0:
    print("Even Parity")
else:
    print("Odd Parity - Error Detection!")
    