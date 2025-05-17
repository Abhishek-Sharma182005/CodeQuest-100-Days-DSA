lst1=list(map(int, input("Enter first list: ").split()))
lst2=list(map(int, input("Enter second list: ").split()))
common_elements=[]
for ele in lst1:
    if ele in lst2 and ele not in common_elements:
        common_elements.append(ele)

if common_elements:
    print("Common elements:", *common_elements)
else:
    print("No common elements found!")
