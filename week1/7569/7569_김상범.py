from collections import deque
import sys

# 상, 하, 좌, 우, 앞, 뒤
dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


N, M, H = map(int, input().split())

box = [[[0] * H for _ in range(N)] for _ in range(M)]
q = deque()
ans = 0
remains = 0

for z in range(H):
    for x in range(M):
        row = list(map(int, input().split()))
        for y, tmp in enumerate(row):
            if tmp == 1:
                q.append((x, y, z))
            elif tmp == 0:
                remains += 1
            box[x][y][z] = tmp

while True:
    nq = deque()
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if (0 <= nx < M) and (0 <= ny < N) and (0 <= nz < H) and box[nx][ny][nz] == 0:
                remains -= 1
                nq.append((nx, ny, nz))
                box[nx][ny][nz] = 1
                # print(nx, ny, nz, end='\t')
    # print()

    if not nq:
        break
    else:
        q = nq
        ans += 1

if remains:
    print(-1)
else:
    print(ans)