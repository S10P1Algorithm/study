from collections import deque


def bfs(row,col):
    cnt = 0 
    visited = [[0]*m for _ in range(n)]
    visited[row][col] = True
    q = deque()
    q.append((row,col))
    cnt_2 = 0
    while q : 
        i,j = q.popleft()
        cnt_2 +=1
        for di,dj in ((0,1),(0,-1),(1,0),(-1,0)):
            ni,nj = i+di, j+dj
            if 0<= ni <n and 0<= nj < m and matrix[ni][nj]==2 and visited[ni][nj]== 0:
                q.append((ni,nj))
                visited[ni][nj] = True
                visited_2[ni][nj] = True
            if 0<= ni < n and 0<= nj < m and matrix[ni][nj]==0 and visited[ni][nj]==0:
                visited[ni][nj] = 3
                # print(ni,nj,111111)
                cnt+=1
    if cnt<=2:  
        res.append((cnt,cnt_2))
n,m = map(int,input().split())

matrix = [list(map(int,input().split() ))for _ in range(n)]
visited_2 = [[0]*m for _ in range(n)]
res =[]
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 2 and visited_2[i][j] == 0:
            bfs(i,j)

print(res)