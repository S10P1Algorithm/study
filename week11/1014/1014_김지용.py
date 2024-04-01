import sys

sys.stdin = open('input.txt', 'r')
from collections import deque

C = int(input())

delta_r = [-1, -1, 0, 0, 1, 1]
delta_c = [-1, 1, -1, 1, -1, 1]


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
            if (nr, nc) not in visited and 0 <= nr < N and 0 <= nc < M and tables[nr][nc] == ".":
                q.append((nr, nc, 1 - stat))
                visited.add((nr, nc))
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
