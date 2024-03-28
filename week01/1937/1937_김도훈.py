import sys
sys.stdin = open("input.txt", "r")

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
arr = [list([0]*N) for _ in range(N)]

stack = []
ans = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 0:
            stack.append((i, j))
        while stack:
            row, col = stack[-1]
            local_max = 0
            for d_r, d_c in delta:
                n_r = row + d_r
                n_c = col + d_c
                if 0<=n_r<N and 0<=n_c<N:
                    if board[n_r][n_c]>board[row][col]:
                        if arr[n_r][n_c]==0:
                            stack.append((n_r, n_c))
                            break
                        else:
                            local_max=max(local_max, arr[n_r][n_c])

            else:
                arr[row][col] = 1 + local_max
                ans = max(ans, arr[row][col])
                stack.pop()


print(ans)