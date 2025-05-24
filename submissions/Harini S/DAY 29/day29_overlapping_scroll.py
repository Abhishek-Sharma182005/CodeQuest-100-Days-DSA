s1=set(map(int,input("Enter first list: ").split()))
s2=set(map(int,input("Enter second list: ").split()))
common=s1&s2
print("Common elements:")
for i in common: print(i,end=" ")