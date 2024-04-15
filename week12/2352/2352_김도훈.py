import sys
sys.stdin = open("input.txt", 'r')

N = int(input())
port = list(map(int, input().split()))

dp = [port[0]]

for i in range(1, N):
    ans = len(dp)
    if port[i] > dp[ans-1]:
        dp.append(port[i])
    else:
        first = 0
        end = ans
        while first < end:
            mid = (first + end ) // 2
            if dp[mid] > port[i]:
                end = mid
            else:
                first = mid + 1
        dp[first] = port[i]

print(len(dp))