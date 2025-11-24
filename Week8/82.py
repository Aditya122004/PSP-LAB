def op(p1,p2,operation='add'):
    res=p1.copy()
    multiplier=1
    if operation=='subtract':
        multiplier=-1
    for exponent,coefficient in p2.items():
        res[exponent]=res.get(exponent,0)+(coefficient*multiplier)
    cleaned_res={}
    for exponent,coefficient in res.items():
        if(coefficient!=0):
            cleaned_res[exponent]=coefficient
    return cleaned_res
p1={3:1,2:3,4:5}
p2={1:1,2:4,3:7}
print(op(p1,p2))