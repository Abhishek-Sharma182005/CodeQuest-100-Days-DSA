numbers= input("Enter frequencies (space-separated): ")
frequencies = list(map(int, numbers.split()))
count={}

for i in frequencies:
    if i in count:
        count[i]+=1
    else:
        count[i]=1

most_common = None
max_count = 0

for i in count:
    if count[i]>max_count:
        max_count=count[i]
        most_common=i

if max_count > 1:
    print(f"Most common frequency: {most_common} (occurs {max_count} times)")
else:
    print("Each frequency occurs only once.")

