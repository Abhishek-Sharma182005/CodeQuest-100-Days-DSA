arr1 = list(map(int, input("Enter first sorted array: ").split()))
arr2 = list(map(int, input("Enter second sorted array: ").split()))

def insertionSort(lst): # Insertion sort
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j+1] = lst[j]
            j = j - 1
        lst[j+1] = key
    return lst

merged = insertionSort(arr1 + arr2)

print("Merged Sorted Array: ", *merged)



