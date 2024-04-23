# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
def high_and_low(numbers):
    number = numbers.split(" ")
    x = sorted(number,key=int)
    
    return x[-1] + " " + x[0]