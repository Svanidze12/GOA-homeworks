# Manual Sum Function: Create a function called manual_sum that iterates over
# list and adds their sum in a variable, then returns variable. Use for loop for this task.
def manualsum(numbers):
    lists = []
    for i in numbers:
        lists.append(i)
    return sum(lists)
print(manualsum([1,4,5,2,8,9]))