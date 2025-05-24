def cipher(sentence,shift):
    result=''
    for i  in sentence:
        if i.isalpha():
            wrap=ord("A") if i.isupper() else ord("a")
            newchr=chr((ord(i)-wrap-shift)%26+wrap)
            result+=newchr
        else: result+=i
    return result
sentence=input("Enter cipher text:")
shift=int(input("Enter shift value:"))
print("Decoded Message:",cipher(sentence,shift))