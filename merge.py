def merge(dict1, dict2):
    dict2.update(dict1)

dict1 = {'a' : 12, 'b' : 1}
dict2 = {'m': 4, 'n' : 9}

merge(dict1, dict2)

print(dict2)