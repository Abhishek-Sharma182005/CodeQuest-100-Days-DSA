a=list(map(int,input("Enter first sorted array: ").split()))
print("Linked Lists: ",end="")
for i in range(len(a)-1):
    print(a[i],end=" -> ")
print(a[-1])