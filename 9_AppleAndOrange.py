s, t = list(map(int, input().split()))
a, b = list(map(int, input().split()))
m, n = list(map(int, input().split()))

mm = list(map(int, input().split()))
nn = list(map(int, input().split()))

cm = cn = 0

cm = sum([1 for m in mm if s <= a + m <= t ])
cn = sum([1 for n in nn if s <= n + n <= t ])



print(cm)
print(cn)
