import sys
input = sys.stdin.readline
from heapq import heappush,heappop

N = int(input())

result = 0
hq = []
for i in range(N):
  h = int(input())
  heappush(hq,(-h,i))
  while hq and -hq[0][0]>h:
    h1,i1 = heappop(hq)
    result = max(result,-h1*(i-i1))
    heappush(hq,(-h,i1))
while hq:
  h,i = heappop(hq)
  result = max(result,-h*(N-i))
print(result)