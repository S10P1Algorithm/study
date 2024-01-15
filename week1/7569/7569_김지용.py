import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    M, N, H = map(int, input().split())
    box = []

    for floor in range(H):
        box.append([])
        for row in range(N):
            box[H].append(list(map(int, input().split())))

    delta_m = [0,0,0,0,-1,1]
    delta_n = [0,0,-1,1,0,0]
    delta_h = [-1,1,0,0,0,0]

    visited = set()
    max_cnt = 0
    def bfs(m, n, h, cnt):
        global visited, max_cnt

        q = deque()
        q.append((m, n, h, cnt))

        while q:
            curr_m, curr_n, curr_h, curr_cnt = q.popleft()
            max_cnt = curr_cnt
            visited.add((curr_m, curr_n, curr_h))
            for i in range(6):
                nm = curr_m + delta_m[i]
                nn = curr_n + delta_m[i]
                nh = curr_h + delta_h[i]
                if 0 <= nm < M and 0 <= nn < N and 0 <= nh < H and \
                        box[nm][nn][nh] == 0 and (nm, nn, nh) not in visited:
                    visited.add((nm, nn, nh))
                    q.append((nm, nn, nh, cnt+1))

