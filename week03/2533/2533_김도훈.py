import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

child = [[] for _ in range(N)]
dp= [[0, 0] for _ in range(N)] 
# dp[i][0] : i 가 inf 일때 최소 inf, dp[i][1] : i 가 inf 아닐때 ""


for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    child[u-1].append(v-1)


def dfs(cur):
    dp[cur] = [1, 0]

    for v in child[cur]:
        dp[cur][0] += min(dfs(v)[1], dfs(v)[0])
        dp[cur][1] += dfs(v)[0]

    return dp[cur]

dfs(0)
print(min(dp[0][0], dp[0][1]))
