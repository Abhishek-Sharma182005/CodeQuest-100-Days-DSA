n=int(input("Enter a number:"))
count=0
for i in range(1,n+1):
    if n%i==0:count+=1
print("Prime") if count==2 else print("Not Prime")