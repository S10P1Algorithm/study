import sys
sys.stdin = open('input.txt', 'r')

N, M, K = map(int, input().split())
board = [input() for _ in range(N)]
gods = [input() for _ in range(K)]

delta = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

dp = [[[{} for _ in range(M)] for _ in range(N)] for _ in range(5)]

for i in range(N):
    for j in range(M):
        dp[0][i][j][board[i][j]] = 1

ans_dict = [{} for _ in range(5)]

for i in range(N):
    for j in range(M):
        temp_val = ans_dict[0].get(board[i][j], 0)
        ans_dict[0][board[i][j]] = temp_val + 1

for l in range(1, 5):
    for i in range(N):
        for j in range(M):
            temp_dict = dp[l-1][i][j]
            for dr, dc in delta:
                row, col = (i + dr) % N, (j + dc) % M
                for key, value in temp_dict.items():
                    new_text = key + board[row][col]
                    temp_val = dp[l][row][col].get(new_text, 0)
                    dp[l][row][col][new_text] = (temp_val + value)



for l in range(1, 5):
    for i in range(N):     
        for j in range(M):
            temp_dict = dp[l][i][j]
            for key, value in temp_dict.items():
                temp_val = ans_dict[l].get(key, 0)
                ans_dict[l][key] = (temp_val + value)

for i in range(K):
    temp = gods[i]
    print(ans_dict[len(temp)-1].get(temp, 0))

