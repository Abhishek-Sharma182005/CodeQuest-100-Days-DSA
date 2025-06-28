def find_anomally(arr):
    diff = arr[1] - arr[0]
    low ,high = 0,len(arr) -1 
    while low <= high :
        mid = (low+high) // 2
        if mid > 0 and arr[mid] - arr[mid -1] != diff:
            print("Anomalous response time detected: ",arr[mid])
            return 
        if mid < len(arr) - 1 and arr[mid + 1] - arr[mid] != diff:
            print("Anomalous response time detected: ",arr[mid + 1])
            return 
        expected = arr[0] + mid * diff
        if arr[mid] == expected:
            low = mid + 1
        else:
            high = mid - 1
    print("No anomally detected ")

nums = list(map(int,input("Enter response times (space-sperated): ").split()))
find_anomally(nums)