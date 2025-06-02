a=list(map(int,input("Enqueue: ").split()))
b=int(input("Dequeue: "))
for i in range(b):
    a.pop(0)
print("Remaining Queue",a)