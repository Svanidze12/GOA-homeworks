# Your task is to make a function that can take any non-negative integer as an argument and return it 
# with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

# Examples:
# Input: 42145 Output: 54421

# Input: 145263 Output: 654321

# Input: 123456789 Output: 987654321


# ეს არის კოდვარის ამოხსნა 

# # def descending_order(num):
#     return int("".join(sorted([num for num in str(num)], reverse=True)))
# Solution
# 1
# def descending_order(num):
# 2
#     # Bust a move righ