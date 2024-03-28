import sys
sys.stdin = open('1937_input.txt')
sys.setrecursionlimit(40000) #

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# DP를 위한 arr 생성
dp = [[0]*N for _ in range(N)]

# dfs 사용
def dfs(x, y):
    # 해당 위치를 이미 방문했다면 return
    if dp[x][y]:
        return dp[x][y]
    else:
        dp[x][y] = 1 #방문하지 않았다면 방문 표시
    # 해당 위치에서 델타 탐색
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        #범위 내이고, 현재 위치의 대나무보다 인접한 위치의 대나무가 더 많은 경우
        if 0 <= nx < N and 0 <= ny < N and arr[x][y] < arr[nx][ny]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1) #현재 dp값과 한칸 이동 dfs값중 큰 걸로 update
    return dp[x][y]

ans = 0

for i in range(N):
    for j in range(N):
        ans = max(ans, dfs(i, j))

print(ans)

