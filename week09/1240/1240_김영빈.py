def dfs(start,end,cnt):
    if start == end:
        # print(cnt)
        return
    for i in graph[start]:
        if visited[i[0]] == 0 :
            visited[i[0]] = visited[start]+i[1]
            # print(graph,'graph')
            # print(visited,'visited')
            cnt += i[1]
            dfs(i[0],end,cnt)
n,m = map(int,input().split())
graph = [[] for _i in range(n+1)]
for i in range(n-1):
    a,b, distance = map(int,input().split())
    graph[a].append((b,distance))
    graph[b].append((a,distance))


for i in range(m):
    visited = [0 for _ in range(n+1)]

    a,b = map(int,input().split())
    visited[a] = 1
    cnt = 0
    dfs(a,b,cnt)
    print(visited[b]-1)