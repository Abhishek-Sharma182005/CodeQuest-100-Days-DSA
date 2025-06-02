string=input("enter a sentence:").lower()
vowels='aeiou'
vow_count,conso_count=0,0
for i in string:
    if i in vowels: vow_count+=1
    else: conso_count+=1
print("Vowels:",vow_count,"\nConsonants:",conso_count)