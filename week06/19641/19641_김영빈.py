import sys

# 재귀적으로 트리를 순회하며 left와 right 필드를 할당하는 함수
def dfs(node, visited):
    global idx
    idx += 1
    left[node] = idx
    for child in graph[node]:
        if not visited[child]:
            visited[child] = True
            dfs(child, visited)
    idx += 1
    right[node] = idx

# 입력 받기
N = int(input())
graph = [[] for _ in range(N + 1)]

# 트리 정보 입력 받기
for _ in range(N):
    edges = list(map(int, input().split()))
    node = edges[0]
    children = edges[1:-1]
    graph[node] = children

root = int(input())

# left와 right 필드를 저장할 리스트 초기화
left = [0] * (N + 1)
right = [0] * (N + 1)

# 방문 여부를 나타내는 리스트 초기화
visited = [False] * (N + 1)
visited[root] = True

# 순회 인덱스 초기화
idx = 0

# DFS 수행하여 left와 right 필드 할당
dfs(root, visited)

# 결과 출력
for i in range(1, N + 1):
    print(i, left[i], right[i])
