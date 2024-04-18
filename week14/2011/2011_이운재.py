arr = list(map(int, list(input())))

ln = len(arr)

dp = [0] * (ln + 1)

if arr[0] == 0:
    print(0)
else:
    arr = [0] + arr
    # print(arr)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, ln+1):
        cur = arr[i]
        cur2 = arr[i-1] * 10 + arr[i]

        if 0 < cur < 10:
            dp[i] += dp[i-1]

        if 10 <= cur2 <= 26:
            dp[i] += dp[i-2]

        dp[i] %= 1000000

    print(dp[ln])
