import sys

sys.stdin = open('input.txt', 'r')
from collections import deque

C = int(input())

delta_r = [-1, -1, 0, 0, 1, 1]
delta_c = [-1, 1, -1, 1, -1, 1]

delta_r2 = [1, -1]
delta_c2 = [0, 0]


def bfs(start_r, start_c):
    global visited, pairs, delta_r, delta_c
    bin1 = 0
    bin2 = 0
    q = deque()
    q.append((start_r, start_c, 0))
    visited.add((start_r, start_c))
    while q:
        row, col, stat = q.popleft()
        if stat == 0:
            bin1 += 1
        elif stat == 1:
            bin2 += 1
        for delta in range(6):
            nr = row + delta_r[delta]
            nc = col + delta_c[delta]
            if (nr, nc) not in visited and 0 <= nr < N and 0 <= nc < M and tables[nr][nc] != "x":
                q.append((nr, nc, 1 - stat))
                visited.add((nr, nc))
        for delta2 in range(2):
            nr2 = row + delta_r2[delta2]
            nc2 = col + delta_c2[delta2]
            if (nr2, nc2) not in visited and 0 <= nr2 < N and 0 <= nc2 < M and tables[nr2][nc2] != "x":
                q.append((nr2, nc2, stat))
                visited.add((nr2, nc2))

    pairs += max(bin1, bin2)


for test_case in range(C):
    N, M = map(int, input().split())
    tables = [input().strip() for _ in range(N)]

    pairs = 0

    visited = set()
    for i in range(N):
        for j in range(M):
            if (i, j) not in visited and tables[i][j] == ".":
                bfs(i, j)

    print(pairs)
