a1=list(map(int,input("Enter first sorted array:").split()))
a2=list(map(int,input("Enter second sorted array:").split()))
merged_list=[]
i,j=0,0
while i<len(a1) and j<len(a2):
    if a1[i]<a2[j]:
        merged_list.append(a1[i])
        i+=1
    else: 
        merged_list.append(a2[j])
        j+=1
merged_list.extend(a1[i:])
merged_list.extend(a2[j:])
print("Merged Sorted Array:",end=" ")
for i in merged_list: print(i,end=" ")