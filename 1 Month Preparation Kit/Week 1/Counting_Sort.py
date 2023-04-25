def countingSort(arr):
    sorted = []
    
    for i in range(100):
        total = arr.count(i)
        sorted.append(total)
    return sorted

print(countingSort([1, 2, 2, 4, 5]))