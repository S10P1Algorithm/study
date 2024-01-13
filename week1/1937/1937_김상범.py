import sys
sys.setrecursionlimit(200000)
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    if visited[x][y]:
        return visited[x][y]

    ret = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] > matrix[x][y]:
            if visited[nx][ny]:
                ret = max(ret, visited[nx][ny] + 1)
            else:
                ret = max(ret, dfs(nx, ny) + 1)

    visited[x][y] = ret
    return ret


ans = 1
for i in range(N):
    for j in range(N):
        ans = max(ans, dfs(i, j))

print(ans)