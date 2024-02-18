import sys
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N):
    arr = list(map(int, input().split()))
    start = arr[0]

    dest = arr[1:]

    i = 0
    while dest[i] != -1:
        graph[start].append(dest[i])
        i += 1

    graph[start].sort()

root = int(input())

visited = set()
euler = [[0, 0] for _ in range(N+1)]
parent = [0 for _ in range(N+1)]

stack = []

stack.append(root)
cnt = 1

while stack:

    node = stack.pop()
    visited.add(node)

    euler[node][0] = cnt
    cnt += 1

    while graph[node] and graph[node][-1] in visited:
        graph[node].pop()


    if not graph[node]:
        euler[node][1] = cnt
        cnt += 1
        euler[parent[node]][1] = cnt
        cnt += 1

    while graph[node]:
        neighbor = graph[node].pop()
        if neighbor not in visited:
            stack.append(neighbor)
        else:
            parent[node] = neighbor


for j in range(1, N+1):
    print(j, ' '.join(map(str, euler[j])))