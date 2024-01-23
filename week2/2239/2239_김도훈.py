import sys
sys.stdin = open('input.txt', 'r')

board = list(list(map(int, input())) for _ in range(9))
delta = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

    
def backtrack(i):
    global ans
    row = i // 9
    col = i % 9
    m_row = (row//3)*3 + 1
    m_col = (col//3)*3 + 1

    if ans:
        return 0
    if i==81:
        ans = True
        for i in range(9):
            print(''.join(map(str, board[i])))
        return 0
    
    if board[row][col] == 0:

        for num in range(1, 10):
            val_num = True
            for j in range(9):
                if board[row][j] == num:
                    val_num = False
                    break
                if board[j][col] == num:
                    val_num = False
                    break

                d_row, d_col = delta[j]
                if board[m_row+d_row][m_col+d_col] == num:
                    val_num = False
                    break
            if val_num:
                board[row][col] = num
                backtrack(i+1)
                board[row][col] = 0
    else:
        backtrack(i+1)

ans = False
backtrack(0)



