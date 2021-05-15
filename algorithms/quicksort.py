def quicksort(arr):
    if len(arr)<2:
        return arr   ### base case
    else:
        pivot = arr[0]
        lesser = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(lesser) + [pivot] + quicksort(greater)


print(quicksort([10, 5 , 8, 2, 0]))
