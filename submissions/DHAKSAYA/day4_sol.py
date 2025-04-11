a=int(input("Enter a nunumber:"))
sum=0
while a!=0:
    temp=int(a%10)
    sum=sum+temp
    a=a/10
print("Sum of digits:",sum)