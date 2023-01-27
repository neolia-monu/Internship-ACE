start = int(input("Enter the start ranges: "))
end = int(input("Enter the end ranges: "))

while start > end:
    start = int(input("Enter the valid start ranges: "))
    end = int(input("Enter the valid end ranges: "))

square = { i: i ** 2 for i in range(start, end+1) }
# vis = { i ** 2: False for i in range(start, end+1) }
print(".....................")
vis = {}

chances = 3

while True and chances > 0:

    print("====== ========= ======== ======")
    user_input = int(input("Enter your input (user): "))

    res = square.get(user_input, 0)
    print("====== ========= ======== ======")

    if res == 0:
        print("The user value is not found")
        chances -= 1
    elif vis.get(user_input, False) == True:
        print("The value is already visited")
        chances -= 1
    else:
        print("Congratulations you find your number: ", str(res))
        vis[user_input] = True
    print("")

print("..........")
print("Your chances are over :(")