def count_occurrences(collection, search_term):
    count = 0
    for item in collection:
        if item == search_term:
            count += 1
    return count


collection = [1, "fruit", 3, 4, 2, 2, 3, 5]
search_term = "fruit"
print(count_occurrences(collection, search_term))