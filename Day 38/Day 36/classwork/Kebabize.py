def kebabize(st):
    word = ""
    for i in st:
        if i.isalpha() == False:
            i = ""
        if i.isupper():
            i = i.lower()
            word +="-" + i
        else:
            word += i
    return word.strip("-")