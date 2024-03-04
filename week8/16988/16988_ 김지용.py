import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

visited = set()
white_group = set()

for i in range(N):
    for j in range(M):
