from collections import deque
import sys

input=sys.stdin.readline

def topology_sort(n, m, edges):
    # 각 노드의 진입 차수를 저장할 리스트
    in_degree = [0] * (n + 1)
    # 각 노드에서 다른 노드로 가는 간선 정보를 저장할 리스트
    graph = [[] for _ in range(n + 1)]
    # 결과를 저장할 리스트
    result = []

    # 간선 정보를 입력받아 그래프를 구성하고, 진입 차수를 업데이트
    for x, y in edges:
        graph[x].append(y)
        in_degree[y] += 1

    # 진입 차수가 0인 노드를 큐에 삽입
    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)

    # 위상 정렬 실행
    while queue:
        # 큐에서 원소 꺼내기
        node = queue.popleft()
        result.append(node)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for next_node in graph[node]:
            in_degree[next_node] -= 1
            # 새롭게 진입 차수가 0이 된 노드를 큐에 삽입
            if in_degree[next_node] == 0:
                queue.append(next_node)

    # 결과 출력
    for node in result:
        print(node, end=' ')


n, m = map(int, input().split())  # 노드 수, 간선 수 입력 받기
edges = []
for _ in range(m):
    x, y = map(int, input().split())
    edges.append((x, y))
topology_sort(n, m, edges)