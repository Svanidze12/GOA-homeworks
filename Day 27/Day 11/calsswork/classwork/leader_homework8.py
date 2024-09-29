num = int(input("enter your random number here: "))

if num % 2 == 0 and num % 3 != 0:
    print("it can be devided into 2")
elif num % 3 == 0 and num % 2 != 0:
    print("it can be devided into 3")
elif num % 2 == 0 and num % 3 == 0:
    print("this number devided to both")