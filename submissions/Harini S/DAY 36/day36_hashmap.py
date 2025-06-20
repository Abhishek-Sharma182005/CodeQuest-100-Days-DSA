sentence_list=list(map(str,input("Enter the sentence:").lower().split()))
count_items={}
for item in sentence_list:
    if item in count_items:
        count_items[item]+=1
    else:
        count_items[item]=1
for key,value in count_items.items():
    print(key,":",value)