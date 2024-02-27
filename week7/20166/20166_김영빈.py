from collections import deque
def dfs(i,j,res,length,cnt):
    queue = deque([(i,j)])
    text=matrix[i][j]
    idx = 1
    print(queue,321)
    while len(text) < length:
        i,j = queue.popleft()
        for di,dj in ((0,1),(0,-1),(-1,0),(1,0),(-1,-1),(1,1),(-1,1),(1,-1)):
            ni,nj = i+di, j+dj
            if ni == -1 :
                ni = m-1
            if ni == m :
                ni = 0
            if nj == -1:
                nj = n-1
            if nj == n:
                nj = 0
            print(ni,nj,idx)
            if matrix[ni][nj] == res[idx]:
                idx +=1
                queue.append((ni,nj))
                text+=matrix[ni][nj]
            if len(text) == length:
                break
            if text == res:
                cnt+=1
                break

    print(queue)

n,m,k = map(int,input().split())
matrix = [input() for _ in range(n)]

texts = [input() for _ in range(k)]
for _ in range(k):
    cnt=0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == texts[_][0]:
                print(len(texts[_]),23)
                dfs(i,j,texts[_],len(texts[_]),cnt)

    print(cnt,1)