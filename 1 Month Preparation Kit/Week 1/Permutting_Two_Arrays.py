def twoArrays(k, A, B):
    A.sort(reverse=True)
    B.sort()
    
    zipped = zip(A, B)
    counter = 0
    
    for t in zipped:
        if t[0] + t[1] >= k:
            counter += 1
    
    if counter == len(A):
        return "YES"
    
    return "NO"

print(twoArrays(10, [2, 1, 3], [7, 8, 9]))