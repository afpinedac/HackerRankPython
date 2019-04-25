input()
l = list(map(int, input().split()))

p = n = z = 0, 0, 0
for e in l:
    if (e > 0):
        p += 1
    elif (e < 0):
        n += 1
    else:
        z += 1

s = '\n'.join([str(format(x / len(l), '.6f')) for x in [p, n, z]])

print(s)
