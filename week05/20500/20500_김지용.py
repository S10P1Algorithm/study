N = int(input())

if N == 1:
    print(0)
else:
    dp = [[0]*3 for _ in range(N)]

    dp[1][1] = 1
    dp[1][2] = 1

    for i in range(2, N):
        dp[i][0] = dp[i-1][1] + dp[i-1][2]
        dp[i][1] = dp[i-1][0] + dp[i-1][2]
        dp[i][2] = dp[i-1][0] + dp[i-1][1]


    print(dp[N-1][1] % 1000000007)