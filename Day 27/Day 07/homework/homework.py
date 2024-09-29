#გამოიტანე 1დან 10მდე ლუწი რიცხვები range_ს დახმარებით
#1
for i in range(0,10,2):
    print(i)

#გამოიტანე while ციკლის მეშვეობით გამოიტანეთ 1დან-20მდე ციფრები
#2
    
i = 1

while i < 20:
    print(i)
    i = i + 1

# while ციკლის მეშვეობით ნულიდან ხუთის ჩათვლით შეკრიბეთ ციფრები
#3

counter = 1  
summation = 0
while counter <= 5:
    print(counter)
    summation = counter + summation
    counter = counter + 1
    print(summation)

#for ციკლში გამოიყენეთ რაიმე string და გატესტეთ როგორ მუშაობს იგი (გამოიტანეთ სტრინგის თითო სიმბოლო ყოველ იტერაციაზე) 
#4

for i in range(12):
    print("goa")
for i in "goa":
    print(i)
    








