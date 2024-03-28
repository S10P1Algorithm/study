from collections import deque

#탐색을 위한 dx, dy, dz
#순서대로 좌, 우, 상, 하, 앞, 뒤
delta = [(-1, 0, 0), (1, 0, 0), (0, 0, 1), (0, 0, -1), (0, -1, 0), (0, 1, 0)]

#bfs
def bfs():
    while Queue:
        x, y, z = Queue.popleft()
        for d in range(6):
            nx, ny, nz = x + delta[d][0], y + delta[d][1], z + delta[d][2]
            # 상자 범위 내에
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
                # 익지 않은 사과가 있다면,
                if tomato_box[nz][ny][nx] == 0:
                    # 1은 익은 사과, 2는 1일차에 익은 사과,
                    # ... 따라서 ans는 max(tomato_box) - 1 임
                    tomato_box[nz][ny][nx] = tomato_box[z][y][x] + 1
                    Queue.append((nx, ny, nz))

M, N, H = map(int, input().split())

#가로 M, 세로 N, 높이 H인 토마토 박스
tomato_box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
#좌표를 담을 Queue 생성
Queue = deque()

#초기 토마토 좌표를 Queue에 담기
for z in range(H):
    for y in range(N):
        for x in range(M):
            if tomato_box[z][y][x] == 1:
                Queue.append((x,y,z))
#탐색(bfs)
bfs()

#tomato_box에 0이 하나라도 남아있다면, 익지않은 것이고
#다 익었다면, 최댓값 - 1이 답이 됨
ans = 0

for z in range(H):
    for y in range(N):
        for x in range(M):
            #익지 않았다면 답을 출력하고 종료
            if tomato_box[z][y][x] == 0:
                print(-1)
                exit()
            ans = max(ans, tomato_box[z][y][x])

print(ans-1)