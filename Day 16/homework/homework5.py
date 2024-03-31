#5) შექმენით replace ფუნქციის კოპიო

# text = ["i", "like", "messi"]
# x = ["ronaldo"]

# print(text[0] + " " +  text[1] + " " + x[0])


def replace_function(word):
    my_list = ["messi", "is",  "goat"]
    my_list[0] = word
    return my_list
    
print(replace_function("ronaldo"))