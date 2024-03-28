from copy import deepcopy

def is_enemy(arr):

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                return True
    return False

def kill(arr,i,j,p,k):
    dead = 0
    for x in range(M):
        flag = True
        for y in range(N-1,-1,-1):
            if abs(y-N) + abs(x-i) <= k and arr[y][x] == 1:
                dead += 1
                arr[y][x] = 0
                flag = False
                break
        if not flag:
            break

    for x in range(M):
        flag = True
        for y in range(N-1,-1,-1):
            if abs(y-N) + abs(x-j) <= k and arr[y][x] == 1:
                dead += 1
                arr[y][x] = 0
                flag = False
                break
        if not flag:
            break

    for x in range(M):
        flag = True
        for y in range(N-1,-1,-1):
            if abs(y-N) + abs(x-p) <= k and arr[y][x] == 1:
                dead += 1
                arr[y][x] = 0
                flag = False
                break
        if not flag:
            break
    return dead

def move(arr):
    for i in range(N-1,0,-1):
        for j in range(M):
            arr[i][j] = arr[i-1][j]
            arr[i-1][j] = 0
    for i in range(M):
        arr[0][i] = 0
N, M, k = map(int,input().split())

arr = []


for i in range(N):
    arr.append(list(map(int,input().split())))
arr.append([0] * M)
max_v = 0
# 궁수위치 설정
for i in range(M-2):
    for j in range(i+1, M-1):
        for p in range(j+1, M):
            ans = 0
            tmp = deepcopy(arr)
            tmp[N][i] = 1
            tmp[N][j] = 1
            tmp[N][p] = 1

            while is_enemy(tmp):
                # 사냥
                ans += kill(tmp,i,j,p,k)
                move(tmp)

            if ans > max_v:
                max_v = ans

print(max_v)
