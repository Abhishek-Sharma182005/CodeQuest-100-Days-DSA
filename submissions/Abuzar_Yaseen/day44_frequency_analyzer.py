frequency = input("Enter frequency: ")
input_freq = list(map(int,frequency.strip().split()))\

count = {}

for freq in frequency:
    if freq in count:
        count[freq] += 1
    else:
        count[freq] = 1

max_count = max(count.values())

most_common_freq = []
for freq in count:
    if count[freq] == max_count:
        most_common_freq.append(freq)

if max_count == 1:
    print("Each frequency occurs only once: ")
else:
    for freq in most_common_freq:
        print(f"Most common frequency:{freq} (occurs {max_count} times)")