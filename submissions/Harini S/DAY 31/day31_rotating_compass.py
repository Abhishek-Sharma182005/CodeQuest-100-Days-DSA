num=list(map(int,input("Enter numbers:").split()))
k=int(input("Enter rotation value (K):"))
k=k%len(num)
rotated_arr=num[-k:]+num[:-k]
print("Rotated Array:")
for i in rotated_arr: print(i,end=" ")
