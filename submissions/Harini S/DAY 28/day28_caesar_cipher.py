def decoder(text,shift):
    res=""
    for i in text:
        if i.isalpha():
            wrap=ord("A") if i.isupper() else ord("a")
            new=chr((ord(i)-wrap-shift)%26+wrap)
            res+=new
        else:
            res+=i
    return res
sentence=input("Enter cipher text: ")
shift=int(input("Enter shift value:"))
print(decoder(sentence,shift))
