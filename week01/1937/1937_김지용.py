n = int(input())

board = []

for i in range(n):
    board.append(tuple(map(int, input().split())))

result = 0

delta_r = [-1, 1, 0, 0]
delta_c = [0, 0, -1, 1]


def is_stop(row, col):
    for i in range(4):
        nr = row + delta_r[i]
        nc = col + delta_c[i]
        if 0 <= nr < n and 0 <= nc < n and board[nr][nc] > board[row][col]:
            return False
    return True


def backtrack(row, col, cnt):
    global result
    if is_stop(row, col):
        result = max(result, cnt)
    else:
        curr = board[row][col]
        for i in range(4):
            nr = row + delta_r[i]
            nc = col + delta_c[i]
            if 0 <= nr < n and 0 <= nc < n and board[nr][nc] > curr:
                cnt += 1
                backtrack(nr, nc, cnt)
                cnt -= 1


for i in range(n):
    for j in range(n):
        if not is_stop(i, j):
            backtrack(i, j, 1)

print(result)
