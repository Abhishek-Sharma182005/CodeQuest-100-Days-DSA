def quick_sort(array):
    if len(array) <= 1:
        return array  
    else:
        pivot = array[0]  
        left = [x for x in array[1:] if x <= pivot] 
        right = [x for x in array[1:] if x > pivot]  
        return quick_sort(left) + [pivot] + quick_sort(right) 

arr = list(map(int, input("").split()))
sorted_array = quick_sort(arr)
print(*sorted_array)