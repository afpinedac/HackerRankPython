n = int(input())

for _ in range(0, n):

    g = int(input())

    if g <= 37:
        print(g)
    elif (g + 1) % 5 == 0:
        print(g + 1)
    elif (g + 2) % 5 == 0:
        print(g + 2)
    else:
        print(g)
