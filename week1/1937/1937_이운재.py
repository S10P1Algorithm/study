import sys
sys.setrecursionlimit(100000)

dx = [1,-1,0,0]
dy = [0,0,1,-1]


def dfs(x,y):
    # 중간부터 시작하면 재는게 의미 없음. 
    if visited[x][y]:
        return visited[x][y]

    # 놓아지는곳은 무조건 이용하니 디폴트는 1
    area = 1 
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and bamboo[nx][ny] > bamboo[x][y]:
            if visited[nx][ny]:
                area = max(area, visited[nx][ny] + 1)
            else:
                area = max(area, dfs(nx, ny) + 1)

    visited[x][y] = area
    return area



N = int(input())

visited = [[0] * N for _ in range(N)]
bamboo = []

for i in range(N):
    bamboo.append(list(map(int,input().split())))

max_v = 0

for i in range(N):
    for j in range(N):
        max_v = max(max_v, dfs(i,j))

print(max_v)