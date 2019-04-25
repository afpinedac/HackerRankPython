sa = list(map(int, input().split()))
sb = list(map(int, input().split()))

s = [0, 0]
for a, b in zip(sa, sb):
    if (a > b):
        s[0] += 1
    elif (a < b):
        s[1] += 1

print(*s)
