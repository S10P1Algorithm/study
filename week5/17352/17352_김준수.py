from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = list([] for _ in range(N+1))
if N - 2 != 0:
    for _ in range(N - 2):
        p1, p2 = map(int, input().split())
        arr[p1].append(p2)
        arr[p2].append(p1)

visited = list([False]*(N+1))

queue = deque()

queue.append(1)
visited[1] = True

while queue:
    now = queue.popleft()
    for next in arr[now]:
        if visited[next]:
            continue
        queue.append(next)
        visited[next] = True

for i in range(2, N+1):
    previous_group = visited[i-1]
    if previous_group != visited[i]:
        print(f'{i-1} {i}')
        break
