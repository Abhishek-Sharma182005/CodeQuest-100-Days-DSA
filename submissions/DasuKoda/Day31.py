a=list(input("Enter the list : "))
k=int(input("enter the num :"))
c=a[-k:]+a[:-k]
result=''.join(str(i) for i in c)
print(result)

'''
Enter the list : 12345
enter the num :2
45123


'''