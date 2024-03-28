from collections import deque
import sys
input = sys.stdin.readline

delta = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 0, 1), (0, 1, 0), (0, 0, -1)]

M, N, H = map(int, input().split())
box = []
for _ in range(H):
    box.append([list(map(int, input().split())) for _ in range(N)])

dq = deque()
for h in range(H):
    for i in range(N):
        for j in range(M):
            if box[h][i][j] == 1:
                dq.append((h, i, j))

while dq:
    ch, ci, cj = dq.popleft()
    for d in delta:
        nh, ni, nj = ch+d[0], ci+d[1], cj+d[2]
        if 0<=nh<H and 0<=ni<N and 0<=nj<M:
            if box[nh][ni][nj] != 0:
                continue
            box[nh][ni][nj] = box[ch][ci][cj] + 1
            dq.append((nh, ni, nj))

nono = False
maximum = 0
for h in range(H):
    for i in range(N):
        for j in range(M):
            if box[h][i][j] == 0:
                nono = True
            elif maximum < box[h][i][j]:
                maximum = box[h][i][j]

print(maximum - 1 if nono == False else -1)
