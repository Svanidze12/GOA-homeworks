# 6) შექმენით join ფუნქციის კოპიო, (ვიცი რომ არ იცით მაგრამ 
#დასერჩეთ და ისწავლეთ. შემდეგ გაკვეთილზე აგიხსნით
def copy_join(list):
    word = ""
    for i in list:
        word = word +  i + " "
    return word
print(copy_join(["pc", "football", "woman", "goa", "man"]))