# Make a program that filters a list of strings and returns a list with only your friends name in it.

# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...
def friend(x):
    lst = []
    for i in x:
        if len(i) == 4:
            lst.append(i)
    return lst
    


