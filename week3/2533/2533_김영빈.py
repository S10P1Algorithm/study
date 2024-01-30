# 트리dp어케하누
N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

print(graph)
