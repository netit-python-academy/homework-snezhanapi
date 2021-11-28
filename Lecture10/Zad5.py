d2 = {'a':1, 'b':2, 'c':4}
d1 = {'a':1, 'b':2, 'c':3}
result = {}
for (key1, val1), (key2, val2) in zip(d1.items(), d2.items()):
    if key1  == key2 and val1 !=val2:
        list = val1,val2
        result = {key1: list }
print(result)