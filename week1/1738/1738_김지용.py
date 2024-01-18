import sys
import heapq

# 다익스트라 사용
# 비용을 마이너스로 하여 최소힙을 사용하였다.

input = sys.stdin.readline

n, m = map(int, input().split())

min_cost = -1000*n

graph = [[] for _ in range(n+1)]
cost = [min_cost]*(n+1)

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

q = []
waypoint = []
heapq.heappush(q, (0, 1))
cost[1] = 0
while q:
    curr_cost, curr_point = heapq.heappop(q)
    if cost[curr_point] < curr_cost:
        continue
    for next_node in graph[curr_point]:
        new_cost = curr_cost + next_node[1]
        if new_cost < cost[next_node[0]]:
            waypoint.append(next_node[0])
            cost[next_node[0]] = new_cost
            heapq.heappush(q, (new_cost, next_node[0]))

print(waypoint)

            


