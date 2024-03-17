#შექმენით ორი ცვლადი name - password სადაც მომხარებელს შემოატანიებთ სახელს და პაროლს და ასევე შექმენით მესამე 
#ცვლადი repeat_password სადაც თუ მომხმარებელის შეყვანილი პაროლი არ დაემთხვევა პირველად შეყვანილ პაროლს 
#დაუწერეთ რომ პაროლი არასწორია თუარადა დაუწერეთ "თქვენ წარმატებით გაიარეთ რეგისტრაცია" \


name = input("enter yourn name here: ")
password = input("enter your pass here: ")
repeat_password = input("enter your password again: ")

if password != repeat_password:
    print("ar sheesabameba")
else: 
    print("sheesabameba")
    



