N = int(input())


dp = [[[0] * (1 << 10) for _ in range(10)] for _ in range(N)]

MOD = 1000000000

for i in range(1, 10):
    dp[0][i][0|1<<i] = 1



for i in range(N-1):
    for j in range(10):
        for k in range(1<<10):
            if j+1 <= 9:
                dp[i+1][j+1][k|1<<(j+1)] +=  dp[i][j][k]
                dp[i+1][j+1][k|1<<(j+1)] %= MOD
            if j-1 >= 0:
                dp[i+1][j-1][k|1<<(j-1)] += dp[i][j][k]
                dp[i+1][j-1][k|1<<(j-1)] %= MOD


ans = 0
for i in range(10):
    ans += dp[N-1][i][(1<<10) -1]
    ans %= MOD
print(ans)