d1 = {'a':1, 'b':'b', 'z':[1], 'd':{'a':'b', 'c':'b'}, 'j': {1,3,5}}
d2 = {'e': 45 ,'b':'c', 'z':[2], 'd':{'h':'a', 'c':'a'}, 'j': {2,4}, 'p':True}
d3 = {'e': 45 ,'b':'c', 'z':[2], 'd':{'h':'a', 'c':'a'}, 'j': {2,4}, 'p':1}
from copy import deepcopy

def merge(x, y):
    z = {}
    overlapping_keys = x.keys() & y.keys()
    for key in overlapping_keys:
        assert(type(x[key]) == type(y[key]))
        if isinstance(x[key], dict) and isinstance(y[key], dict):
            z[key] = merge(x[key], y[key])
        elif isinstance(x[key], list):
            z[key] = x[key]
            z[key].extend(y[key])
        elif isinstance(x[key], set):
            z[key] = x[key]|y[key]
        else:
            z[key] = y[key]
            
    for key in x.keys() - overlapping_keys:
        z[key] = deepcopy(x[key])
    for key in y.keys() - overlapping_keys:
        z[key] = deepcopy(y[key])
    return z
    
print(merge(d1,d2))
