import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

adj = [[] for _ in range(n+1)]
inDegree = [0 for _ in range(n+1)]
que = deque()
res = []

for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    adj[a].append(b)
    inDegree[b] += 1

for i in range(1, n+1):
    if inDegree[i] == 0:
        que.append(i)

while que:
    temp = que.popleft()
    res.append(temp)
    for i in adj[temp]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            que.append(i)

print(*res)