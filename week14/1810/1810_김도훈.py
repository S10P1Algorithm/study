import sys
import heapq
sys.stdin = open("input.txt", "r")

N, dest = map(int, input().split())
vert_cord = [(0, 0, 0)] # x, y, idx
adj_list = [[] for _ in range(N + 1)]
ans = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    vert_cord.append((x, y, i+1))

# x축 순서로 정렬 후 탐색
vert_cord.sort(key=lambda x: x[0])
for i in range(N):
    for j in range(i + 1, N+1):
        x1, y1, idx_1 = vert_cord[i]
        x2, y2, idx_2 = vert_cord[j]
        if x2 - x1 > 2:
            break
        if abs(y1-y2)<=2:
            dist = (((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)
            adj_list[idx_1].append((idx_2, dist))
            adj_list[idx_2].append((idx_1, dist))

# 다시 idx 순서로
vert_cord.sort(key=lambda x: x[2])
start = 0
dist = [sys.maxsize] * (N + 1)
dist[start] = 0
pq = [(0, start)]

while pq:
    d, u = heapq.heappop(pq)
    if dist[u] < d:
        continue
    if vert_cord[u][1] == dest:
        ans.append(int(round(d, 0)))
    for v, w in adj_list[u]:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            heapq.heappush(pq, (dist[v], v))
if ans:
    print(min(ans))
else:
    print(-1)