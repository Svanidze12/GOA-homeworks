def is_pangram(s):
    s = s.lower()
    is_true = True
    x = "abcdefghijklmnopqrstuvwxyz"
    for i in x:
        if i in s:
            is_true = True
        else:
            is_true = False
            break
    return is_true
