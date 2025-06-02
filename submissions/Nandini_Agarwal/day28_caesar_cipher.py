n = input("Enter cipher text: ")
c = int(input("Enter shift value: "))
print("Decoded Message: ", end="")

for i in n:
    if i.isalpha():
        if i.isupper():
            print(chr((ord(i) - ord('A') - c) % 26 + ord('A')), end="")
        else:
            print(chr((ord(i) - ord('a') - c) % 26 + ord('a')), end="")
    else:
        print(i, end="")