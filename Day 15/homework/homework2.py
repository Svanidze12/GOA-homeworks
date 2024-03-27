#შექმენით ფუნქცია, რომელსაც გადასცემთ სიას. თქვენი დავალებაა, რომ დაბეჭდოთ ამ სიის საშუალო არითმეტიკული (ჯამი / სიგრძე)

def calculate_arithmetic(lst):
    total_sum = sum(lst)
    mean = total_sum / len(lst)
    print("Arithmetic Mean:", int(mean))



my_list = [1, 2, 3, 4, 5]
calculate_arithmetic(my_list)