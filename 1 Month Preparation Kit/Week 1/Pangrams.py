import string

def is_pangram(txt):
    alphabet = dict.fromkeys(string.ascii_lowercase, 0)
    txt = txt.lower()
    
    for i in range(ord('a'), ord('z')+1):
        if chr(i) in txt:
            alphabet[chr(i)] = 1   
        
    if 0 in alphabet.values():
        return 'not pangram'
    else:
        return 'pangram'
    
    
result = is_pangram("We promptly judged antique ivory buckles for the next prize")
print(result)