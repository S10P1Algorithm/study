import sys
sys.stdin = open("input.txt", 'r')

from collections import deque

N = int(input())
board = list(input() for _ in range(N))
delta = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]
# state: 0 일시 세로, 1 일시 가로
def action(row, col, state, move):
    if move == 0:
        return row-1, col, state
    if move == 1:
        return row+1, col, state
    if move == 2:
        return row, col-1, state
    if move == 3:
        return row, col+1, state
    if move == 4:
        return row, col, (state + 1) % 2


def validActionCheck(row, col, state):
    valid_actions = [False, False, False, False, True]
    # 회전가능성 check
    for d_r, d_c in delta:
        n_r = row + d_r
        n_c = col + d_c
        if 0 <= n_r < N and 0 <= n_c < N:
            if board[n_r][n_c] == '1':
                valid_actions[4] = False
                break
        else:
            valid_actions[4] = False
            break

    # 세로
    if state == 0:
        if row > 1:
            if board[row-2][col] != '1':
                valid_actions[0] = True
        if row < N-2:
            if board[row+2][col] != '1':
                valid_actions[1] = True
        if col > 0:
            if board[row][col-1] != '1' and board[row-1][col-1] != '1' and board[row+1][col-1] != '1':
                valid_actions[2] = True
        if col < N-1:
            if board[row][col+1] != '1' and board[row-1][col+1] != '1' and board[row+1][col+1] != '1':
                valid_actions[3] = True
    # 가로
    else:
        if row > 0:
            if board[row-1][col] != '1' and board[row-1][col-1] != '1' and board[row-1][col+1] != '1':
                valid_actions[0] = True
        if row < N-1:
            if board[row+1][col] != '1' and board[row+1][col-1] != '1' and board[row+1][col+1] != '1':
                valid_actions[1] = True
        if col > 1:
            if board[row][col-2] != '1':
                valid_actions[2] = True
        if col < N-2:
            if board[row][col+2] != '1':
                valid_actions[3] = True
    return valid_actions

start = [0, 0, 0]
end = [0, 0, 0]
for row in range(N):
    for col in range(N):
        if board[row][col] == 'B':
            start = [row, col, 0]
        elif board[row][col] == 'E':
            end = [row, col, 0]

if start[1] > 0 and board[start[0]][start[1]-1] == 'B':
    start = [start[0], start[1]-1, 1]
else:
    start = [start[0]-1, start[1], 0]

if end[1] > 0 and board[end[0]][end[1]-1] == 'E':
    end = [end[0], end[1]-1, 1]
else:
    end = [end[0]-1, end[1], 0]

# is_visited[row][col] = [세로, 가로]
is_visited = [[[1E9, 1E9] for _ in range(N)] for _ in range(N)]
q = deque()
q.append(start)
is_visited[start[0]][start[1]][start[2]] = 0

while q:
    row, col, state = q.popleft()
    if row == end[0] and col == end[1] and state == end[2]:
        break
    valid_actions = validActionCheck(row, col, state)
    cnt = is_visited[row][col][state]
    for i in range(5):
        if valid_actions[i]:
            n_r, n_c, n_s = action(row, col, state, i)
            if is_visited[n_r][n_c][n_s] == 1E9:
                q.append([n_r, n_c, n_s])
                is_visited[n_r][n_c][n_s] = cnt + 1

ans = is_visited[end[0]][end[1]][end[2]]
if ans == 1E9:
    print(0)
else:
    print(ans)