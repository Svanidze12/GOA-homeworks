#შექმენით ფუნქცია, რომელსაც გადასცემთ სთრინგს. თქვენი დავალებაა,
#რომ ამ სთრინგს მოაშოროთ ყველა სფეისი - space და დაბეჭდოთ ამ სახით test case: input) " 
#Goal-   Oriented   Academy    " -> output) "Goal-OrientedAcademy"

def info(word):
    x = word.split(" ")
    x = "".join(x)
    print(x)

info("Goal-   Oriented   Academy    " )