test_dict = {"Monu" : [9, 7, 3, 4, 5],
             "Ram" : [6, 7, 4, 3, 3], 
             "Shivam" : [9, 1, 6, 4, 5]}

print(str(test_dict))

max_value = 0
max_key = []

for sub in test_dict:
    dict_val = len(set(test_dict[sub]))
    if dict_val >= max_value:
        max_value = dict_val
        max_key.append(sub)

print("1: Maximum key with unique value:", max_key)

# Lambda function
max_key = sorted(test_dict, key = lambda el : len(set(test_dict[el])))

print(max_key)