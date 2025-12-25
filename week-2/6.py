def all_eq(lst):
    if not lst: return []
    
    max_val = 0
    for s in lst:
        if len(s) > max_val:
            max_val = len(s)
            
    res = []
    for s in lst:
        while len(s) < max_val:
            s += "_"
        res.append(s)
    return res