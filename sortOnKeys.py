nameAgeList = { "shivam" : 21, "nilesh" : 22, "monu" : 20, "manish": 21}

myKeys = list(nameAgeList.keys())
myKeys.sort()

sorted_Dict = {i : nameAgeList[i] for i in myKeys}

print(sorted_Dict)