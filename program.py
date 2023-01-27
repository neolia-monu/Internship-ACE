start = int(input("Enter the start ranges: "))
end = int(input("Enter the end ranges: "))


square = { i: i ** 2 for i in range(start, end+1) }
vis = { i ** 2: False for i in range(start, end+1) }
print(vis)

chances = 3

while True and chances > 0:

    user_input = int(input("Enter your input (user): "))

    res = square.get(user_input, 0)
    if res == 0 or vis.get(user_input) == True:
        chances -= 1
    else:
        print("Congratulations you find your number: ", str(res))
        vis[user_input] = True

print("Your chances are over :(")