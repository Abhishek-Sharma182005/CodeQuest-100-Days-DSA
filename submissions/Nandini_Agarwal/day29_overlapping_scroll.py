a = input("Enter first list: ")
b = input("Enter second list: ")
l=[]
for i in a:
    if i in b:
        l.append(i)
if len(l)>=1:
    print("No common elements found!")
else:
    print("Common elements: ", end="")