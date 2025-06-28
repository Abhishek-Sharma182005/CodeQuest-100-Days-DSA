data = input(("Enter  intervals(format: start-end, space-separated): "))
parts = data.split()
intervals = [list(map(int,p.split('-'))) for p in parts]

intervals.sort()

merged = [intervals[0]]

for curr in intervals[1:]:
    last = merged[-1]
    if curr[0] <= last[1]:
        last[1] = max(last[1],curr[1])
    else:
        merged.append(curr)

print("Merged Intervals: ",end=' ')
for i in merged:
    print(f"[{i[0]},{i[1]}]",end=' ')
