import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
board=[list(input().strip()) for _ in range(N)]
visit=[[[0]*2 for _ in range(N)] for _ in range(N)]
dirs=[(1,0),(0,1),(-1,0),(0,-1),[(1,0),(0,0),(-1,0)],[(0,1),(0,0),(0,-1)]]
slog=[]
dlog=[]
for r in range(N):
    for c in range(N):
        if board[r][c]=='B':
            slog.append((r,c))
        elif board[r][c]=='E':
            dlog.append((r,c))

def toward(r1,r2):
    if abs(r1 - r2) == 1: # 세로방향
        return 1
    else:
        return 0
def check(d1,d2,d3,tt):
    visit[d1[0]][d1[1]][tt] = 1
    visit[d2[0]][d2[1]][tt] = 1
    visit[d3[0]][d3[1]][tt] = 1

for i in range(3):
    s=slog[i]
    visit[s[0]][s[1]][toward(slog[0][0],slog[1][0])]=1

def bfs():
    q = deque()
    slog.append(0)
    q.append(slog)
    while q:
        node=q.popleft()
        n1,n2,n3,cnt=node
        if n1 in dlog and n2 in dlog and n3 in dlog:
            print(cnt)
            return
        for i in range(len(dirs)):
            if len(dirs[i])==3: # 회전
                d1 = (n2[0] + dirs[i][0][0], n2[1] + dirs[i][0][1])
                d2 = (n2[0] + dirs[i][1][0], n2[1] + dirs[i][1][1])
                d3 = (n2[0] + dirs[i][2][0], n2[1] + dirs[i][2][1])
                if 0<=d1[0]<N and 0<=d1[1]<N and 0<=d2[0]<N and 0<=d2[1]<N and 0<=d3[0]<N and 0<=d3[1]<N:
                    if abs(n1[0]-n2[0])==1 and abs(d1[1]-d2[1])==1: # 가로로 회전
                        # 회전할 주변 공간에 벽이 있는지 체크
                        if board[n1[0]][n1[1] - 1] == '1' or board[n2[0]][n2[1] - 1] == '1' or board[n3[0]][n3[1] - 1] == '1':
                            continue
                        if board[n1[0]][n1[1] + 1] == '1' or board[n2[0]][n2[1] + 1] == '1' or board[n3[0]][n3[1] + 1] == '1':
                            continue
                        if visit[d1[0]][d1[1]][0] and visit[d2[0]][d2[1]][0] and visit[d2[0]][d2[1]][0]:
                            continue
                        check(d1,d2,d3,0)
                        q.append([d1,d2,d3,cnt+1])
                    elif abs(n1[1]-n2[1])==1 and abs(d1[0]-d2[0])==1:
                        if board[n1[0]-1][n1[1]]=='1' or board[n2[0]-1][n2[1]]=='1' or board[n3[0]-1][n3[1]]=='1':
                            continue
                        if board[n1[0] + 1][n1[1]] == '1' or board[n2[0] + 1][n2[1]] == '1' or board[n3[0] + 1][n3[1]] == '1':
                            continue
                        if visit[d1[0]][d1[1]][1] and visit[d2[0]][d2[1]][1] and visit[d2[0]][d2[1]][1]:
                            continue
                        check(d1,d2,d3,1)
                        q.append([d1,d2,d3,cnt+1])
            else: # 상하좌우로 이동
                d1 = (n1[0] + dirs[i][0], n1[1] + dirs[i][1])
                d2 = (n2[0] + dirs[i][0], n2[1] + dirs[i][1])
                d3 = (n3[0] + dirs[i][0], n3[1] + dirs[i][1])
                if 0<=d1[0]<N and 0<=d1[1]<N and 0<=d2[0]<N and 0<=d2[1]<N and 0<=d3[0]<N and 0<=d3[1]<N:
                    if board[d1[0]][d1[1]] == '1' or board[d2[0]][d2[1]] == '1' or board[d3[0]][d3[1]] == '1':
                        continue
                    tt = toward(d1[0], d2[0])
                    if visit[d1[0]][d1[1]][tt] and visit[d2[0]][d2[1]][tt] and visit[d3[0]][d3[1]][tt]:
                        continue
                    check(d1,d2,d3,tt)
                    q.append([d1,d2,d3,cnt+1])
    print(0)
bfs()