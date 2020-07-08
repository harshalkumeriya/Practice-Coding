def validitycheck(cid):
    for i in range(3,len(cid),4):
        if cid[i] != '_':
            return "invalid"
            
    L = list(cid.split('_'))

    for j in L:
        for k in j:
            if not (k >= 'a' and k <= 'z') or (k >= 'A' and k <= 'Z') or (k >= 0 and k <= 9):
                return "invalid"
    
    y = set(cid)
    z = list()
    for x in y:
        z.append(cid.count(x))
    if max(z) > 3:
        return "invalid"
    
    return "valid"

cid= 'abc_123_2ac_Adf'
print(validitycheck(cid))
