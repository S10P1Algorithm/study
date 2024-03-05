from collections import deque
from copy import deepcopy

# 이제 돌면서, dfs로 2의 구역을 탐색후 최대값 반환
def dfs(i,j):
    global res
    if visited[i][j]:
        return

    visited[i][j] = 1
    res += 1
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            dfs(nx,ny)


dx = [0,0,1,-1]
dy = [1,-1,0,0]

N, M = map(int,input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]* M for _ in range(N)]
# 놓을 가능성이 있는 흰 돌 위치 리스트 생성

q = deque()
res = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 or arr[i][j] == 1:
            visited[i][j] = 1
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 2:
                    q.append((i,j))
                    break

max_v = 0
for i in range(len(q)-1):
    for j in range(i+1,len(q)):
        tmp = deepcopy(arr)
        tmp[q[i][0]][q[i][1]] = 1
        tmp[q[j][0]][q[j][1]] = 1
        for k in range(N):
            for p in range(M):
                if tmp[k][p] == 2:
                    dfs(k,p)
                    max_v = max(max_v,res)
                    res = 0

print(max_v)



