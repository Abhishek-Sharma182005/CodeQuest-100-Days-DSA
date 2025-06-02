arr =input("Enter the list of integers (space-separated): ").split()
k = int(input("Enter the number of positions to rotate: "))
k = k % len(arr)
rotated_arr = arr[-k:] + arr[:-k]
print("Rotated array:", " ".join(rotated_arr))