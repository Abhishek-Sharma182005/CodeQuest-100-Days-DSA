def merge_lists(arr1,arr2):
    a=sorted(arr1+arr2)
    return list(map(str,a))
a=list(map(int,input("Enter first sorted array: ").split()))
b=list(map(int,input("Enter first sorted array: ").split()))
print("Merged Sorted List:", " ".join(merge_lists(a,b)))