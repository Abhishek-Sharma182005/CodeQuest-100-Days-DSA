a=list(map(int,input("Push: ").split()))
b=int(input("Pop: "))
for i in range(b):
    a.pop(-1)
print("Remaining Queue: ",a)