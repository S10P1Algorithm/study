N, M = map(int, input().split())

m = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if i == 0:
            if j >= m[i]:
                dp[i][j] = c[i]
        else:
            if j < m[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-m[i]]+c[i])

print(dp)