# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces


def get_count(sentence):
    x = "aeiou"
    sum = 0
    for i in sentence:
        for q in x:
            if i == q:
                sum += 1
    return sum