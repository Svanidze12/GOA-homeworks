# Manual Max Function: Define a function named manual_max that iterates through list,
# updating a variable with the maximum value, then returns the maximum value found. 
# Use for loop for this task.
def max_value(max):
    num = 0
    for i in max:
        if i > num:
            num = i
    return num
print(max_value([1,2,3,4,5,7]))