#3) შექმენით ფუნქცია რომელიც გამოითვლის კენტების და ლუწების ჯამს ცალცალკე,
#დააბრუნეთ სია სადაც იქნება ეს ჯამები ჩასმული, შესატანი მონაცემები [1,2,3,4,5] ---- გამოსატანი მონაცემები [6, 9] 


def num(numbers):
    total = 0
    total1 = 0
    for i in range(len(numbers)):
        if i % 2 == 0:
            total = total + numbers[i] 
        elif i % 2 != 0:
            total1 = total1 + numbers[i]
    return total,total1
    
numbers_list = [1, 2, 3, 4, 5]
print(num(numbers_list))