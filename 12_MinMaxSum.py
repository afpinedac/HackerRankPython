ns = list(map(int, input().split()))
ns = sorted(ns)
print("{} {}".format(sum(ns[:-1]), sum(ns[1:])))


