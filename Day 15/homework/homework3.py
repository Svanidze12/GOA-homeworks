#შექმენით ფუნქცია, რომელსაც გადასცემთ სიტყვას და შემოწმდება არის თუ არა ის პალინდრომი 
#(პალინდრომია სიტყვა, თუ მისი შებრუნებულიც იგივე გამოდის, მაგ: level)

def palidrome(word):
    if word == word[::-1]:
        print("palidrome")
    else:
         print("not palidrome")


word = input("enter your word here: ")
palidrome(word)

