from sys import stdin

def xor_2_strings(str1, str2):
    
    result = ""
    
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            result += '0'
        else:
            result += '1'
            
    return result


str1 = stdin.readline().rstrip()
str2 = stdin.readline().rstrip()
    
result = xor_2_strings(str1, str2)    
print(result)