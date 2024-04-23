# Manual Len Function: Develop a function named manual_len that iterates through list,
# counting each element, and returns the count as the length of the list. 
# Use for loop for this task.
def manual_len(word):
    num = 0
    for i in word:
        num = num + i
    return num
print(manual_len([1,2,3,4,5]))