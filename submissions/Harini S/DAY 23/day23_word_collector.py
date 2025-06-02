import re
from collections import Counter
inp_str=input("Enter text:").lower()
remove_punc=re.sub(r'[^\w\s]',' ',inp_str)
count=Counter(remove_punc.split())
for word,occurence in count.items():
    print(word,":",occurence)