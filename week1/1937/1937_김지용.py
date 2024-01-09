from collections import deque

n = int(input())

board = []

for i in range(n):
    board.append(list(map(int, input().split())))

result = n ** 2

delta_r = [-1, 1, 0, 0]
delta_c = [0, 0, -1, 1]


way_board = [[0 for _ in range(n)] for _ in range(n)]

for row in range(n):
    for col in range(n):
        curr = board[row][col]
        is_stop = True
        for k in range(4):
            nr = row + delta_r[k]
            nc = col + delta_c[k]
            if 0 <= nr < n and 0 <= nc < n and curr < board[nr][nc]:
                is_stop = False
                break
        if is_stop:
            way_board[row][col] = 0
        else:
            way_board[row][col] = 1