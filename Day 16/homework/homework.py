#2) შექმენით ფუნქცია რომელიც სიაში ლუწ ინდექსებზე მდგომ რიცხვთა ჯამს 
#დააბრუნებს, შესატანი მონაცემები: [1,2,3,4,5] ---- გამოსატანი მონაცემები (შედეგი):  9 

def num(numbers):
   total = 0
   for i in range (len(numbers)):
      if i % 2 == 0:
         total = total + numbers[i]
         return total
      
numbers_list = [1, 2, 3, 4, 5]
print(num(numbers_list))



