# 친구 관계 그래프
# 얼리어답터이거나 얼리어답터가 아니거나
# 가능한 한 최소의 수의 얼리어답터를 확보
# 친구 관계 트리의 정점 개수 N
# 2 <= N <= 1000000
# 뭔소린지 잘 모르겠음..
# ~~ 얼리 어답터가 아닌 사람들을 자신의 모든 친구들이 얼리 어답터일 때만 아이디어를 받아들임..
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(N-1):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

dp = [[0, 0] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

def dfs(start):
    visited[start] = 1
    if len(arr[start]) == 0:
        dp[start][1] = 1
        dp[start][0] = 0
    else:
        for i in arr[start]:
            if visited[i] == 0:
                dfs(i)
                dp[start][1] += min(dp[i][0], dp[i][1])
                dp[start][0] += dp[i][1]
        dp[start][1] += 1

dfs(1)
print(min(dp[1][0], dp[1][1]))

# dp[현재 노드][얼리어답터 여부 0: 얼리x 1: 얼리]