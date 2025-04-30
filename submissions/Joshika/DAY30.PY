

a = input("Enter cipher text: ")
b = int(input("Enter shift value: "))
c = []

for j in a:
    if 'A' <= j <= 'Z': 
        p = chr((ord(j) - ord('A') - b) % 26 + ord('A'))
    elif 'a' <= j <= 'z': 
        p = chr((ord(j) - ord('a') - b) % 26 + ord('a'))
    else:
        p = j  
    c.append(p)

t = "".join(c)
print("Decoded message:", t)