N = int(input())
M = []

for _ in range(N):
    M.append(list(map(int, input().split())))

dp = [M[i][i] for i in range(N)]
ds = [M[i][N - i - 1] for i in range(N)]

print(abs(sum(dp) - sum(ds)))
