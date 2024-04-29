N = int(input())
graph = []
for _ in range(N):
    graph.append(int(input()))
maximum = 0
for i in range(N):
    w = 0
    h = 0
    extent = 0
    for j in range(1, graph[i]+1):
        if graph[i] == 0:
            break
        h += 1
        for k in range(i, N):
            if graph[k] < h:
                extent = max(extent, w * h)
                w = 0
                break
            w += 1
        else:
            extent = max(extent, w * h)
            w = 0
    else:
        maximum = max(maximum, extent)

print(maximum)
