import sys  # 파이썬 시간초과, 파이파이 통과
import heapq

input = sys.stdin.readline
INF = 10 ** 9
N, F = map(int, input().split())

coordinate = [[0,0,0]]

finish = []

for i in range(1,N+1):
    x,y = map(int, input().split())
    coordinate.append([x,y,i])
    if y == F:
        finish.append(i)

nodes = [[] for _ in range(N+1)]
visited = set()

coordinate.sort()

for i in range(N+1):
    x1,y1,idx1 = coordinate[i]
    for j in range(i+1,N+1):
        x2, y2, idx2 = coordinate[j]
        if abs(x1 - x2) > 2:
            break

        elif abs(x1 - x2) <= 2 and abs(y1 - y2) <= 2:
            cost = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            nodes[idx1].append([idx2, cost])
            nodes[idx2].append([idx1, cost])
            if idx1 < idx2:
                visited.add((idx1, idx2))
            else:
                visited.add((idx2, idx1))

coordinate.sort(key=lambda x: x[1])
for i in range(N + 1):
    x1, y1, idx1 = coordinate[i]
    for j in range(i + 1, N + 1):
        x2, y2, idx2 = coordinate[j]
        if abs(y1 - y2) > 2:
            break

        elif abs(x1 - x2) <= 2 and abs(y1 - y2) <= 2:
            if idx1 < idx2 and (idx1, idx2) in visited:
                continue
            elif idx1 > idx2 and (idx2, idx1) in visited:
                continue

            cost = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            nodes[idx1].append([idx2, cost])
            nodes[idx2].append([idx1, cost])

def Dijkstra():
    distances = [INF for _ in range(N+1)]
    distances[0] = 0
    pq = []
    heapq.heappush(pq, [0, 0])

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)
        if distances[cur_node] < cur_cost:
            continue

        for next_node, next_cost in nodes[cur_node]:
            if distances[next_node] > cur_cost + next_cost:
                distances[next_node] = cur_cost + next_cost
                heapq.heappush(pq, [cur_cost + next_cost, next_node])

    answer = INF
    for g in finish:
        answer = min(answer, distances[g])

    if answer == INF:
        return -1
    else:
        if answer >= int(answer) + 0.5: return int(answer) + 1
        else:
            return int(answer)

print(Dijkstra())