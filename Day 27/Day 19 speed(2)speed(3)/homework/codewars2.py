# Write a function that removes the spaces from the string, then return the resultant string.
def no_space(x):
    word = x.split(" ")
    word = "".join(word)
    return word