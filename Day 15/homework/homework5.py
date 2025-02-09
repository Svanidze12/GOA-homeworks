#შექმენით ფუნქცია, რომელსაც გადასცემთ სიას. ამ სიაში უნდა გქონდეთ როგორც დადებითი, ასევე უარყოფითი რიცხვები.
#თქვენი დავალებაა, რომ გამოიტანოთ უარყოფითი რიცხვების რაოდენობა და 
#დადებითი რიცხვების ჯამი (გამოიყენეთ for ციკლი ორივეზე)


def num(numbers):
    nums = 0
    listn = []
    for i in numbers:
        if i >= 0:
            nums = nums + i 
        else:
            listn.append(i)
            
    print("negative number lenght is ",len(listn))
    print("postive numbers sum is",nums)


my_list = [1, 3, 5, -1, -5]
num(my_list)
