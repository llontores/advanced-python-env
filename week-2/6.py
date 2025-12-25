lst = ["a", "abcd", "ab"]

if not lst: 
    print([]) 
else:
    max_val = 0
    for s in lst:
        if len(s) > max_val:
            max_val = len(s)
            
    res = []
    for s in lst:
        new_s = s
        while len(new_s) < max_val:
            new_s += "_"
        res.append(new_s)
    
    print(res)