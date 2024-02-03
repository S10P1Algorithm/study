N, M = map(int,input().split())

memory = [0] + list(map(int,input().split()))
cost = [0] + list(map(int,input().split()))

length = sum(cost) + 1

arr = []
dp = [[0 for _ in range(length)] for _ in range(N+1)]

max_v = 10001

for i in range(1, N+1):
    cost_v, memory_v = cost[i], memory[i]
    for j in range(length):
        dp[i][j] = dp[i-1][j]
    for j in range(cost_v, length):
        dp[i][j] = max(dp[i-1][j-cost_v] + memory_v, dp[i][j])
        if dp[i][j] >= M:
            max_v = min(max_v, j)

print(max_v)

# 냅색 알고리즘을 잘 기억해두자. 그것뿐




