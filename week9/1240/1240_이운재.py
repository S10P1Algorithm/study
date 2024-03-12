
def dfs(x,y, distance):
    visited[x] = True
    if x == y:
        print(distance)
        return

    for i in graph[x]:
        if visited[i[0]] == False:
            distance += i[1]
            dfs(i[0],y, distance)
            distance -= i[1]

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]


for i in range(N-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))


for i in range(M):
    visited = [False] * (N + 1)
    node1,node2 = map(int,input().split())
    dfs(node1,node2,0)




