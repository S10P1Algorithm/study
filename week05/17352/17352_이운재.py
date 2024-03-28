from collections import  deque
import sys
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]

check = [0]*(N+1)

if N-2 != 0:
    for i in range(N-2):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)


q = deque()

q.append(1)
check[1] = True

while q:
    now = q.popleft()
    for next in graph[now]:
        if check[next]:
            continue
        q.append(next)
        check[next] = True

for i in range(1,N+1):
    if not check[i]:
        print(i, i-1)
        break

# 단순하게 풀어도 풀림 ;;