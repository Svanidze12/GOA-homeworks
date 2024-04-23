# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for
def find_short(s):  
    words = s.split(" ")
    word_len = len(words[0])
    for word in words:
        if len(word) < word_len:
            word_len = len(word)
            print(word_len)
    return word_len