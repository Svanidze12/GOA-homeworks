# Given a non-empty array of integers,
# return the result of multiplying the values together in order. 
def grow(arr):
    total = 1
    for i in arr:
        total = total * i
    return total
    