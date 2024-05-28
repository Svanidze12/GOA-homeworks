# Detect Panagram
def is_pangram(s):
    letters = "abcdefghijklmnopqrstuvwxyz"
    is_true = True
    for i in letters:
        if i in s.lower():
            is_true = True
        else:
            is_true = False
            break
    return is_true


# Duplicate Encoder


def duplicate_encode(word):
    word = word.lower()
    x = ""
    for i in word:
        if word.count(i) > 1:
            x += ")"
        elif word.count(i) == 1:
            x += "("
    return x


#First non-repeating character

def first_non_repeating_letter(s):
    string = ""
    for i in s:
        if s.lower().count(i.lower()) == 1:
            string = string + i
    if string == "":
        return string
    else:
        return string[0]