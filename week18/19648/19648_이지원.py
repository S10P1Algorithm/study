from collections import defaultdict, deque

N = int(input())

inf = 1 << 10
mod = 1000000007

edges = [[5], [0, 5, 10], [1], [2], [3], [0, 9], [1, 3, 7, 11, 12],
         [3, 8], [3, 4], [10], [6, 11], [12], [7, 13], [8]]

e_len = [1, 3, 1, 1, 1, 2, 5, 2, 2, 1, 2, 1, 2, 1]

dist = [[inf for _ in range(14)] for _ in range(14)]

for i in range(14):
    dist[i][i] = 0
    for j in edges[i]:
        dist[i][j] = 1

# 플로이드 워셜
for k in range(14):
    for i in range(14):
        for j in range(14):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

cnt = 0
dp = defaultdict(list)

for i in range(14):
    for j in range(i+1, 14):
        key = frozenset((i, j))
        for u in edges[i]:
            for v in edges[j]:
                if dist[u][v] >= 3 and dist[v][u] >= 3:
                    dp[key].append((u, v))

que = deque()
que.append((1, 7, 0))

while que:
    a, b, r = que.popleft()
    if r < N:
        for x, y in dp[frozenset((a, b))]:
            que.append((x, y, r+1))
            cnt += 1
            cnt %= mod

print(cnt)
    


