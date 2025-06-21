arr=list(map(int, input("Enter numbers: ").split()))
if arr[0]>arr[1] :
    max1=arr[0]
    max2=arr[1]
else:
    max2=arr[0]
    max1=arr[1]

for i in range(2, len(arr)):
    if arr[i]>max1:
        max2=max1
        max1=arr[i]
    elif arr[i]>max2:
        max2=arr[i]

print("Second Largest Number: ",max2)