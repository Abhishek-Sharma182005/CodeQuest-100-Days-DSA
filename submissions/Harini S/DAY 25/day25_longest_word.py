sentence_list=list(map(str,input("Enter a sentence:").split()))
length=0
for i in sentence_list:
    if len(i)>length:
        length+=1
        word=i
print("Longest word:",i)