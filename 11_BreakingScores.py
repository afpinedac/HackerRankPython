input()
scores = list(map(int, input().split()))

bh = bl = 0
max = min = scores[0]

for score in scores:
    if score < min:
        bl += 1
        min = score

    if score > max:
        bh += 1
        max = score

print(bh, bl)
