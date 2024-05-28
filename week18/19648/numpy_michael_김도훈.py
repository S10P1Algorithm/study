import sys
import numpy as np
sys.stdin = open("input.txt", "r")
V = 14
G = [(1, 2, 4), (2,), (1, 3), (4,), (5, 12), (6,), (7, 13), (8,), (9, 10), (10,), (11,), (0,), (0, 5, 6, 10, 13), (8, 10)]
A, B = 0, 1
Mod = 10**9 + 7

dist = [[15]*14 for _ in range(14)]

# 초기화
for i in range(V):
    dist[i][i] = 0
    for j in G[i]:
        dist[i][j] = 1
# Floyd-warshall
for k in range(V):
    for i in range(V):
        for j in range(V):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

pair = []
for i in range(V):
    for j in range(V):
        if dist[i][j] >=3 and dist[j][i] >= 3:
            pair.append((i, j))

N = len(pair)

temp = [[0]*N for _ in range(N)]
ans_arr = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            ans_arr[i][j] = 1
        if pair[j][0] in G[pair[i][0]] and pair[j][1] in G[pair[i][1]]:
            temp[i][j] = 1


t = int(input())
np_temp = np.array(temp, dtype=np.int64)
np_ans = np.array(ans_arr, dtype=np.int64)
for k in range(30):
    if t & 1<<k:
        np_ans = np.dot(np_ans, np_temp) % Mod

    np_temp = np.dot(np_temp, np_temp) % Mod

ans = 0
for j in range(N):
    ans += np_ans[4][j]
    ans %= Mod
print(ans)