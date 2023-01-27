import sys

start = int(input("Enter the start ranges: "))
end = int(input("Enter the end ranges: "))

# while start > end:
#     start = int(input("Enter the valid start ranges: "))
#     end = int(input("Enter the valid end ranges: "))
if start > end:
    print("Program exit because of the invalid input")
    sys.exit(0)

square = { i: i ** 2 for i in range(start, end+1) }
# vis = { i ** 2: False for i in range(start, end+1) }
print(".....................")
vis = set()

chances = 3

while True and chances > 0:

    print("====== ========= ======== ======")
    user_input = int(input("Enter your input (user): "))

    res = square.get(user_input, -1) # change from 0 to -1
    print("====== ========= ======== ======")

    if res == -1:
        print("The user value is not found")
        chances -= 1
    elif user_input in vis:
        print("The value is already visited")
        chances -= 1
    else:
        print("Congratulations you find your number: ", str(res))
        vis.add(user_input)
        chances = 3 # reset chance
    print("")

print("..........")
print("Your chances are over :(")