import sys
sys.setrecursionlimit(10**5)
sys.stdin = open("input.txt", 'r')

N = int(input())
G = list(map(int, input().split()))
MOD = 10**9 + 7

adj_list = [[] for _ in range(N)]
dp= [[[0, 0], [0, 0], 0] for _ in range(N)]
# dp[i][0] : i 가 O 일때 [gcd, n], dp[i][1] : i 가 X 일때 [gcd, n]
is_visited = [False for _ in range(N)]
is_visited[0] = True
dp[0] = [[G[0], 1], [G[0], 0], 0]

for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    adj_list[u-1].append(v-1)
    adj_list[v-1].append(u-1)

def gcd(a, b):
    while b!= 0:
        a, b = b, a % b
    return a

def dfs(cur):
    for v in adj_list[cur]:
        if not is_visited[v]:
            curr = G[v-1]
            dp[v][0][1] = dp[cur][0][1] + 1
            dp[v][1][1] = dp[cur][0][1] + dp[cur][1][1]
            a = gcd(curr, dp[v][0][0])
            b = gcd(curr, dp[v][1][0])
            # 갯수 * gcd
            temp = ((dp[cur][0][1] * a) + (1 * b) + (dp[cur][0][1] * dp[cur][0][0]) + (dp[cur][1][1] * dp[cur][1][0])) % MOD
            dp[v][2] = temp
            is_visited[v] = True
            print(v, temp)
            dfs(v)

dfs(0)
# for i in range(N):
#     print(dp[i][2])
print(dp)