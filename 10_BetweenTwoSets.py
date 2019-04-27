input().split()

a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))

c = 0
for i in range(1, 101):

    if (all([i % j == 0 for j in a1]) and all([j % i == 0 for j in a2])):
        c += 1

print(c)
