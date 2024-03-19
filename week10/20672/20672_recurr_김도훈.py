import sys
sys.setrecursionlimit(10**5)
sys.stdin = open("input.txt", 'r')

N = int(input())
G = list(map(int, input().split()))
GCD = [G[0]]

def gcd(a, b):
    while b!= 0:
        a, b = b, a % b
    return a

for i in range(1, N):
    GCD.append(gcd(G[0], G[i]))
GCD = list(set(GCD))
GCD.sort()
GCD_L = len(GCD)

GCD_dict = {}
for i in range(GCD_L):
    GCD_dict.setdefault(GCD[i], i)
print(GCD_dict)

MOD = 10**9 + 7
adj_list = [[] for _ in range(N)]
dp= [[[0, 0] for _ in range(GCD_L)] for _ in range(N)]

is_visited = [False for _ in range(N)]
is_visited[0] = True
for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    adj_list[u-1].append(v-1)
    adj_list[v-1].append(u-1)

def dfs(cur):
    temp = gcd(G[0], G[cur])
    if not is_visited[cur-1]:
        dp[cur][GCD_dict[temp]][0] = 1
        dp[cur][GCD_dict[G[0]]][1] = 1
        is_visited[cur] = True

    for v in adj_list[cur]:
        if not is_visited[v]:
            dfs(v)
            for i in range(GCD_L):
                tmp_local = gcd(temp, GCD_dict[i])
                dp[cur][tmp_local][0] = (dp[cur][tmp_local][0] * dp[v][GCD_dict[i]][0]) + 
                dp[cur][tmp_local][1] = 

                dp[v][GCD_dict[i]][0]
                dp[v][GCD_dict[i]][1]

# dfs(0)

print(dp)