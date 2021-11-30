d2 = {'a':1, 'b':2, 'c':4}
d1 = {'a':1, 'b':2, 'c':3}
result = {}

for key1, val1 in d1.items():
    if key1 in d2.keys():
        if val1 != d2[key1]:
            list = val1, d2[key1]
            result[key1] = list
    else:
        list = val1, None
        result[key1] = list
for key2, val2 in d2.items():
    if key2 in d1.keys():
        pass
    else:
        list = None,val2
        result[key2] = list
#for (key1, val1), (key2, val2) in zip(d1.items(), d2.items()):
  #  if key1  in d2 and val1 !=val2:
  #      list = val1,val2
    #     result = {key1: list }
if result:
    print(sorted(result.items()))
else:
    print(result)