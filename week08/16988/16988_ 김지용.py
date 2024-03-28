import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

visited = set()
empty = set()
white_group = set()

del_r = [0, 0, 1, -1]
del_C = [1, -1, 0, 0]
def dfs(start_row, start_col):
    global visited
    dfs_visited = set()
    dfs_empty = set()
    visited.add((start_row, start_col))
    dfs_visited.add((start_row, start_col))
    stack = [(start_row, start_col)]

    while stack:
        row, col = stack.pop()
        for i in range(4):
            nrow = row + del_r[i]
            ncol = col + del_C[i]
            if 0 <= nrow < N and 0 <= ncol < M:
                if board[nrow][ncol] == 2 and (nrow, ncol) not in visited:
                    dfs_visited.add((nrow, ncol))
                    visited.add((nrow, ncol))
                    stack.append((nrow, ncol))
                elif board[nrow][ncol] == 0 and (nrow, ncol) not in dfs_empty:
                    dfs_empty.add((nrow, ncol))
    return len(dfs_visited), dfs_empty


for i in range(N):
    for j in range(M):
        if (i, j) not in visited and board[i][j] == 2:
            l, e  = dfs(i, j)
            empty.union(e)
            white_group.add((l, tuple(e)))

le = len(empty)
empty_list = list(empty)
max_cnt = 0

for i in range(le-1):
    for j in range(i+1, le):
        curr_empty1 = empty_list[i]
        curr_empty2 = empty_list[j]
        curr_cnt = 0
        for k in white_group:
            curr_blank = k[1]
            if curr_empty1 in curr_blank:
                k[1].remove(curr_empty1)
            elif curr_empty2 in curr_blank:
                k[1].remove(curr_empty2)
        for l in white_group:
            if l[1] == []:
                curr_cnt += l[1]
        max_cnt = max(max_cnt, curr_cnt)

print(max_cnt)






