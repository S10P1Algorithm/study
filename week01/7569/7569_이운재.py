# 1 = 익은 토마토, 0 = 익지 않은 토마토 , -1 = 토마토가 들어있지 않음.

import copy
import sys
input = sys.stdin.readline
#상하좌우 위 아래


M,N,H = map(int, input().split())

dx = [1,-1,0,0,N,-N]
dy = [0,0,1,-1,0,0]
tomato = []

for i in range(H):
    for j in range(N):
        tomato.append(list(map(int,input().split())))

day = 0
while True:

    tmp = copy.deepcopy(tomato)
      
    for i in range(N*H):
        for j in range(M):
            if tomato[i][j] == 1:
                
                for k in range(6):
                    ni = i + dx[k]
                    nj = j + dy[k]

                    
                

                    if 0 <= ni < N*H and 0 <= nj < M :
                        if tomato[ni][nj] == 0:
                            tomato[ni][nj] = 1
                

    if tmp == tomato:
        break
    else:
        day += 1

for i in range(N*H):
        for j in range(M):
            if tomato[i][j] == -1:
                day = -1
                break
        if day == -1:
            break

print(day)
