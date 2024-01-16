import copy
from collections import deque
M,N,H = map(int,input().split()) # M :가로 , N : 세로 , H : 높이
# 1: 익은 토마토 , 0 : 익지 않은 토마토 , -1 : 토마토가 들어 있지 않은 칸
tomatoes = [list(map(int, input().split())) for _ in range(N) for _ in range(H)]
q=deque()
for i in range(N*H):
    for j in range(M):
        if tomatoes[i][j] == 1:
            q.append((i,j))


delta = [(0,1), (0,-1), (1,0), (-1,0), (-N,0), (N,0)]
cnt = 0
check_1 = 1 # 처음부터 다 익었는지

for w in range(N*H):
    for x in range(M):
        if tomatoes[w][x] == 0 :
            check_1 = 0 
if check_1 == 1:
    print(0)
else:
    while q:
        check = 0 # 토마토 다 익었는지 체크
        p = copy.deepcopy(q)
        
        while p :
            # print(p)
            q.popleft()
            i,j = p.popleft()
            # print(i,j)
            # for i in range(N*H) :
            #     for j in range(M):
            
            for di,dj in delta :
                # print(di,dj)
                ci = i + di
                cj = j + dj
                if (0<=ci<N*H and 0<=cj<M) :
                    if tomatoes[ci][cj] == 0 :
                        tomatoes[ci][cj] = 1
                        
                        q.append((ci,cj))
        cnt+=1
        # for _ in tomatoes:
        #     print(_)
        # print(cnt)

        for a in range(N*H):
            for b in range(M):
                if tomatoes[a][b] == 0 :
                    check = 1
        
        if check == 0 : 
            break
        
    for i in range(N*H):
        for j in range(M):
            if tomatoes[i][j]  == 0 :
                # print(-1)
                cnt=-1
                break
        
    print(cnt)
        