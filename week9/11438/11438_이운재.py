from collections import deque
import sys

input = sys.stdin.readline

N = int(input())

parent = [0] * (N + 1)
level = [0] * (N + 1)
visited = [0] * (N + 1)
tree = [[] for _ in range(N+1)]

for i in range(N-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

def bfs(s):
    q = deque()
    q.append(s)
    while q:
        node = q.popleft()
        visited[node] = True
        for i in tree[node]:
            if not visited[i]:
                level[i] = level[node] + 1
                parent[i] = node
                q.append(i)
def LCA(a,b):
    if level[a] < level[b]:
        a,b = b, a

    diff = level[a]-level[b]
    for _ in range(diff):
        a = parent[a]
    while a != b:
        a = parent[a]
        b = parent[b]
    return a

bfs(1)

M = int(input())
for i in range(M):
    a,b = map(int,input().split())
    print(LCA(a,b))


## 시간초과