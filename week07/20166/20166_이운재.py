import sys
input = sys.stdin.readline

dx = [1,-1,0,0,1,1,-1,-1] #상하좌우,우상,좌상,우하,좌하
dy = [0,0,1,-1,1,-1,1,-1]

N, M, K = map(int,input().split())

world = [list(input().rstrip()) for _ in range(N)]

target =[input().rstrip() for _ in range(K)]

cnt = 0
def dfs(x,y,now,target):
    global cnt

    now += world[x][y]

    if len(now) == len(target):
        if now == target:
            cnt += 1
        return
    else:
        if now != target[:len(now)]:
            return
    
    for  i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0:
            nx += N
        elif nx >= N:
            nx -= N
        
        if ny < 0:
            ny += M
        elif ny >= M:
            ny -= M
        
        dfs(nx,ny,now,target)
god = dict()
for tg in target:
    if tg in god.keys():
        print(god[tg])
        continue
    for i in range(N):
        for j in range(M):
            dfs(i,j,'',tg)
    god[tg] = cnt
    print(cnt)
    cnt = 0