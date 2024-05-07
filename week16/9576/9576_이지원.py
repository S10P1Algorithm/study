import sys
from heapq import heappush, heappop

tc = int(input())
    
for _ in range(tc):
    N, M = map(int, input().split())
    visited = [False for _ in range(N+1)]
    heap = []
    ans = 0
    for _ in range (M):
        a, b = map(int, input().split())
        heappush(heap,(b, a))
           
    while heap:
        b, a = heappop(heap)
        
        for i in range(a, b+1):
            if not visited[i]:
                visited[i] = True
                ans += 1
                break
    
    print(ans)