import sys
input = sys.stdin.readline

N = int(input())

visited = set()

dp = [[[0 for _ in range(1024)] for _ in range(10)] for _ in range(N+1)]

for i in range(1, 10):
    dp[1][i][1 << i] = 1

for j in range(2, N+1):
    for k in range(10):
        for l in range(1024):
            if k == 0:
                dp[j][0][l|1<<0] += dp[j-1][1][l]
            elif k == 9:
                dp[j][9][l|1<<9] += dp[j-1][8][l]
            else:
                dp[j][k][l|1<<k] += dp[j-1][k-1][l] + dp[j-1][k+1][l]

result = 0

for h in range(10):
    result += dp[N][h][1023]

print(result % 1000000000)