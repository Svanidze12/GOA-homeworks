# 2) შექმენით ფუნქცია რომელსაც გადაეცემა list = ["name1" , "name2" , "name3"....] 
# შემდეგ მომხმარებელს კითხეთ რომელი ინდექსის შეცვლა სურს და ამის მიხედვით შეცვალეთ
# ის კონკრეტული ინდექსი თქვენი სასურველი 
# სტრინგით და ბოლოს შეაერთეთ join() ფუნქციის მეშვეობით


def modify_list(lst):
    print("Old List:", lst)
    index = int(input("Enter the index you want to change: "))
    new_value = input("Enter the new value: ")
    lst[index] = new_value
    result = " ".join(lst)
    print("New List:", result)

names_list = ["avto", "goa", "dato"]
modify_list(names_list)

 