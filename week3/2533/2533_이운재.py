import sys

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]

while True:
    try:
        a,b = map(int,input().split())
        graph[a].append(b)
    except:
        break

print(graph)
