import sys
from collections import deque
input = sys.stdin.readline

# 위상 정렬
# 방향성을 가진 그래프, 내부에 순환이 없는 그래프
# 1. 진입 차수가 0인 정점을 큐에 삽입한다.
# 2. 큐에서 원소를 꺼내 해당 원소에 연결된 간선을 제거한다.
# 3. 간선을 제거한 후 진입 차수가 0이 된 정점을 큐에 삽입한다.
# 4. 위 과정을 반복한다.

N, M = map(int, input().split())
# 단방향 간선을 나타낼 그래프
graph = [[] for _ in range(N+1)]
# 진입 차수(외부에서 특정 노드로 들어오는 간선의 개수)를 나타내는 1차원 리스트
inDegree = [0]*(N+1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    inDegree[B] += 1

q = deque()

for s in range(1, N+1):
    # 진입 차수가 0인 노드들을 큐에 넣음
    if inDegree[s] == 0:
        q.append(s)

ans = []

while q:
    s = q.popleft()
    ans.append(s)

    for adj_s in graph[s]:
        # 간선 제거
        inDegree[adj_s] -= 1
        # 진입 차수가 0이 된 노드를 큐에 삽입
        if inDegree[adj_s] == 0:
            q.append(adj_s)

print(*ans, sep=" ")
