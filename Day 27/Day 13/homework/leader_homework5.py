num = int(input("Write a number from 1 to 10"))

if num < 1 or num > 10:
    print("your number is incorrect")

for i in range(1,50):
    if i % num == 0:
       print(i)