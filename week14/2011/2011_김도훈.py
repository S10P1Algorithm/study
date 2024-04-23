import sys

code = list(map(int, input()))
N = len(code)
mod = 1000000
if N == 1:
    if code[0] == 0:
        ans = 0
    else:
        ans = 1
else:
    dp = [0] * N
    if code[0] == 0:
        ans = 0
    else:
        dp[0] = 1
        if code[1] == 0:
            if code[0] == 1 or code[0] == 2:
                dp[1] = 1
            else:
                dp[1] = 0
        else:
            if code[0] == 1:
                dp[1] = 2
            elif code[0] == 2:
                if code[1] <= 6:
                    dp[1] = 2
                else:
                    dp[1] = 1
            else:
                dp[1] = 1
        if N < 2:
            ans = dp[1]
        else:
            for i in range(2, N):
                if code[i] == 0:
                    if code[i-1] == 1 or code[i-1] == 2:
                        dp[i] = dp[i-2]
                    else:
                        ans = 0
                        break
                else:
                    if code[i-1] == 1:
                        dp[i] = (dp[i-1] + dp[i-2]) % mod
                    elif code[i-1] == 2:
                        if code[i] <= 6:
                            dp[i] = (dp[i-1] + dp[i-2]) % mod
                        else:
                            dp[i] = dp[i-1]
                    else:
                        dp[i] = dp[i-1]
            else:
                ans = dp[-1]
print(ans % mod)