def binarySearch(arr, start, end, x):

    while start <= end:
        mid = (start + end)//2

        if arr[mid] == x:
            return mid

        elif arr[mid] < x:
            start = mid + 1

        else:
            end = mid -1

    return -1


arr = [-5, 3.0, 10, 20, 50, 80]
x = 3
result = binarySearch(arr, 0, len(arr), x)
print(result)

arr = [0, 1, 0]  #### doesn't work correctly if multiple instances of a number present
