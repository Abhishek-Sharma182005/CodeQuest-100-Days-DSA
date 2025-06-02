l=list(map(int,input("Enter Numbers:").split()))
tot=0
for i in range(1,len(l),2):tot+=l[i]
print("Hidden Key:",tot)