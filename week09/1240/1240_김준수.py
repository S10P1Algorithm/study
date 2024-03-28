from collections import deque


def bfs(start, target):
    queue = deque()
    queue.append((start, 0))
    visited = [0] * (N+1)
    visited[start] = 1
    while queue:
        node, c_distance = queue.popleft()

        if node == target:
            return c_distance

        for n_node, n_distance in graph[node]:
            if visited[n_node]:
                continue
            visited[n_node] = 1
            queue.append((n_node, n_distance + c_distance))


# 노드의 개수 N, 노드 쌍의 개수 M 입력
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

# N-1 개의 연결된 두 점과 거리 입력
for _ in range(N-1):
    node1, node2, distance = map(int, input().split())
    graph[node1].append((node2, distance))
    graph[node2].append((node1, distance))

# M개의 타겟 노드 쌍 입력
for _ in range(M):
    node1, node2 = map(int, input().split())
    print(bfs(node1, node2))
