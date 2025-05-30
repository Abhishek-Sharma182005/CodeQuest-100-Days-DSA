# Input : take space separated integers from the user
numbers = list(map(int, input("Enter numbers: ").split()))
even_position_sum = 0
for index in range (1,len(numbers) + 1):
    if index % 2 == 0:
        even_position_sum += numbers[index - 1]
print("Hidden key:",even_position_sum)        