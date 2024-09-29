def collatz(n):
    lists = [str(n)]
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        lists.append(str(int(n)))
    return "->".join(lists)