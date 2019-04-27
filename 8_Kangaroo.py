x1, v1, x2, v2 = list(map(int, input().split()))

found = False
for i in range(1, 10001):

    if x1 + (v1 * i) == x2 + (v2 * i):
        found = True
        break

print('YES' if found else 'NO')