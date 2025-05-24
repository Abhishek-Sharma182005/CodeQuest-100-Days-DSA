arr = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter rotation value (K): "))

k = k % len(arr) # Normalize k to ensure it is within bounds of array length

# Right rotate the array by k
right_rotate = arr[-k:] + arr[:-k]
left_rotate  = arr[k:] + arr[:k]


print("Right Rotated Array:", *right_rotate)  # * -> it unpacks the list to a set of values
print("Left Rotated Array:", *left_rotate)