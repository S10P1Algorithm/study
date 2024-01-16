from collections import deque
import sys

# 상, 하, 좌, 우, 앞, 뒤
dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

'''
3차원 M, N, H크기의 토마토가 있음 안익은 토마토가 있을 수 있어서 안익은 토마토들은 인접한 토마토의 영향을 받아서 익게된다. 
'''
# y, x, z 값 받기
N, M, H = map(int, input().split())

# x, y, z값 만큼의 배열 생성
box = [[[0] * H for _ in range(N)] for _ in range(M)]

# 익은 과일 큐 설정
q = deque()
ans = 0
remains = 0

# 큐브 값 전처리 
for z in range(H):
    for x in range(M):
        row = list(map(int, input().split()))
        # 한 행을 받아옴 
        for y, tmp in enumerate(row):
            # 행의 열번호, 값을 분해
            # 값이 1일경우 익은 과일 큐에 추가
            if tmp == 1:
                q.append((x, y, z))
            # 값이 0일 경우 익어야 하는 개수에 추가
            elif tmp == 0:
                remains += 1
            box[x][y][z] = tmp

while True:
    nq = deque()
    # 섞이지 않기위해 새로운 큐 사용
    
    # bfs
    while q:
        x, y, z = q.popleft()
        # 6방향인게 특징
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if (0 <= nx < M) and (0 <= ny < N) and (0 <= nz < H) and box[nx][ny][nz] == 0:
                remains -= 1
                nq.append((nx, ny, nz))
                box[nx][ny][nz] = 1
                # print(nx, ny, nz, end='\t')

    # 익은 토마토가 전부 영향을 끼쳤을때 
    # 새롭게 익은 큐가 있는가?
    if not nq:
        # yes일시 중지
        break
    else:
        # no일시 큐는 nq
        q = nq
        # 시간 + 1
        ans += 1
        
# 종료후 익어야할 과일이 남아있는가?
if remains:
    print(-1)
else:
    print(ans)