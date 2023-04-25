def birthday(s, d, m):
    if len(s) == m:
        if sum(s) == d:
            return 1
        else:
            return 0
    
    if sum(s[0:m]) == d:
        return birthday(s[1:], d, m) + 1
    else:
        return birthday(s[1:], d, m)

    
    
s = [5, 1, 4, 1, 5, 4, 5, 1, 3, 5, 1, 1, 5, 1, 4, 2, 1, 1, 1, 2, 5]
d = 15
m = 7

print(birthday(s, d, m))