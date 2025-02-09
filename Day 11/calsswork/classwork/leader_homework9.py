num = int(input("compare numbers here"))
num2 = int(input("please type second type here"))
operation = input("type any compare")


if operation == "<":
    print(num < num2)
elif operation == ">":
    print(num > num2)
elif operation == "=":
    print(num = num2)
elif operation == "!=":
    print(num != num2)