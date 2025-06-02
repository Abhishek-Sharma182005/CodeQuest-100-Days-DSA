num = input("Enter numbers: ")
input_line = list(map(int,num.strip().split()))

unique = list(set(input_line))

unique.sort(reverse=True)
second_largest = unique[1]
print("Second Largest Number: ",second_largest)

