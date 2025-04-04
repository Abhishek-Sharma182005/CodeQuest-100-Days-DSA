a=int(input("Enter a number:"))
sum=0
while a!=0:
    d=a%10
    sum+=d
    a=a//10
print("Security key:",sum)