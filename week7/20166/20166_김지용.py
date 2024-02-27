import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = []
god = []

for _ in range(N):
    arr.append(list(input().strip()))

for _ in range(K):
    god.append(input())

