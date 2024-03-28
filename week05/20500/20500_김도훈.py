N = int(input())
dp = [[0] * 15 for _ in range(N)]
dp[0][1] += 1
dp[0][5] += 1

for i in range(1, N):
    for j in range(15):
        dp[i][(10 * j + 1) % 15] = (dp[i][(10 * j + 1) % 15] + dp[i-1][j]) % 1000000007
        dp[i][(10 * j + 5) % 15] = (dp[i][(10 * j + 5) % 15] + dp[i-1][j]) % 1000000007

print(dp[N-1][0])