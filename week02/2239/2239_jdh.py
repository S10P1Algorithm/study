import sys
input = sys.stdin.readline

#각 행에 1~9가 하나씩 있는지 확인하는 함수
def row_checking(row, num):
    for col in range(9):
        if num == sudoku_table[row][col]:
            return False
    return True

#각 열에 1~9가 하나씩 있는지 확인하는 함수
def col_checking(col, num):
    for row in range(9):
        if num == sudoku_table[row][col]:
            return False
    return True

#각 구역(3*3)에 1~9가 하나씩 있는지 확인하는 함수
def square_checking(row, col, num):
    # start_row, start_col는 출발 지점으로 0 3 6에서 시작할 수 있도록 선언
    start_row, start_col = row // 3 * 3, col // 3 * 3
    for i in range(3):
        for j in range(3):
            if num == sudoku_table[start_row+i][start_col+j]:
                return False
    return True

def dfs(i):
    # 종료조건 (빈 좌표를 다 돌았을 경우)
    if i == len(blanks):
        for j in range(9):
            print(''.join(map(str, sudoku_table[j])))
        exit()

    for num in range(1, 10):
        row, col = blanks[i][0], blanks[i][1]

        if row_checking(row, num) and col_checking(col, num) and square_checking(row, col, num):
            sudoku_table[row][col] = num
            dfs(i+1)
            sudoku_table[row][col] = 0

blanks = []
sudoku_table = [list(map(int, input().rstrip())) for _ in range(9)]

for i in range(9):
    for j in range(9):
        if sudoku_table[i][j] == 0:
            blanks.append((i,j))

dfs(0)
