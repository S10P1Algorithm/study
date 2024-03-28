import sys
sys.stdin = open("input.txt", "r")

from collections import deque

adj = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]
M, N, H = list(map(int, input().split()))
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

que = deque()
for k in range(H):
    for j in range(N):
        for i in range(M):
            if arr[k][j][i] == 1:
                que.append((i, j, k))


while que:
    tmt = que.popleft()
    tmp = arr[tmt[2]][tmt[1]][tmt[0]]

    for d_i, d_j, d_k in adj:        
        n_i, n_j, n_k = tmt[0] + d_i, tmt[1] + d_j, tmt[2] + d_k
        if 0 <= n_i < M and 0 <= n_j < N and 0 <= n_k < H and arr[n_k][n_j][n_i] == 0:
            arr[n_k][n_j][n_i] = tmp + 1
            que.append((n_i, n_j, n_k))

ans = True
for k in range(H):
    for j in range(N):
        for i in range(M):
            if arr[k][j][i] == 0:
                ans = False
                break
        if ans==False:
            break
    if ans==False:
        break

if ans:
    print(tmp-1)
else:
    print(-1)
