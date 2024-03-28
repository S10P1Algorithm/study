N, M = map(int, input().split())
active = [0] + list(map(int, input().split()))
deactive = [0] + list(map(int, input().split()))
length = sum(deactive) + 1
dp = [[0 for _ in range(length)] for _ in range(N + 1)]
ans = 10001

for i in range(1, N + 1):
    memory = active[i]
    cost = deactive[i]
    for j in range(length):
        dp[i][j] = dp[i - 1][j]
    for j in range(cost, length):
        dp[i][j] = max(dp[i - 1][j - cost] + memory, dp[i][j])
        if dp[i][j] >= M:
            ans = min(ans, j)

print(ans)

#-----------
print(dp)


# https://lcyking.tistory.com/37
# 냅색 알고리즘