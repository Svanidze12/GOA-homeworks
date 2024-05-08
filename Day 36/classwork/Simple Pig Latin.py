def pig_it(text):
    
    texts = text.split(" ")
    word = ""
    
    for i in texts:
        if i in "!%&.?":
            word = word + i
        else:
            i= i[1:]+ i[0] + "ay"
            word = word + i + " "
            
    return word.strip()