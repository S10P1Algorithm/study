import sys
sys.stdin = open('input.txt', 'r')
import heapq
from collections import deque

n, m = list(map(int, input().split()))

gph = [{} for _ in range(n+1)]
edge = []
vert = [0] * (n+1)
n_connected = [False]*n
rev_connection = [[] for _ in range(n)]
n_cycle = False

for _ in range(m):
    u, v, w = list(map(int, input().split()))
    gph[u].setdefault(v, -w)
    edge.append([u, v, -w])
    rev_connection[v-1].append(u-1)

# n번 노드로 갈 수 있는지 확인
n_connected[n-1] = True
que = deque()
que.append(n-1)

while que:
    u = que.popleft()
    for v in rev_connection[u]:
        if not n_connected[v]:
            n_connected[v] = True
            que.append(v)

    

# 0번노드 추가후 벨만포드로 음의 사이클 확인
for v in range(1, n+1):
    if n_connected[v-1]:
        gph[0].setdefault(v, 0)


for iter in range(1, n+1):
    for e in edge:
        u, v, w = e
        if vert[u] + w < vert[v]:
            vert[v] = vert[u] + w
            if iter == n and n_connected[v-1]:
                n_cycle = True


# 음의 사이클 없다면 cost 양수로 변환 후 다익스트라
if not n_cycle and n_connected[0]:
    for u in range(1, n+1):
        for v in gph[u].keys():
            gph[u][v] = gph[u][v] + vert[u] - vert[v]


    vert = [20000000] * (n+1)
    vert[0] = vert[1] = 0
    prev = [0] * (n+1)

    hq = []
    heapq.heappush(hq, (0, 1))
    while hq:
        min_v = heapq.heappop(hq)[1]
        if min_v == n:
            break
        for v in gph[min_v].keys():
            if vert[min_v] + gph[min_v][v] < vert[v]:
                vert[v] = vert[min_v] + gph[min_v][v]
                heapq.heappush(hq, (vert[v], v))
                prev[v] = min_v

    path = []
    curr = n
    while curr!=1:
        path.append(curr)
        curr = prev[curr]
    path.append(1)
    print(*path[::-1])
else:
    print(-1)