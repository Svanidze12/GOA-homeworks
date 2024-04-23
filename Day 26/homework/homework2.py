# Manual Min Function: Define a function named manual_min that iterates through list,
# updating a variable with the minimum value, then returns the minimum value found.
# Use for loop for this task.
def minimal_value(min):
    num = 1
    for i in min:
        if i < num:
            num = i
    return num
print(minimal_value([1,2,3,4,5,8,7]))

