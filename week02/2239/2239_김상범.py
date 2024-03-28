def backtracking(row, col):
    global sudoku, rows, columns, area

    # 행이 9일 때 스도쿠가 완성된 상태이므로 True 반환
    if row == 9:
        return True
    
    # 현재 위치에 숫자가 이미 존재하는 경우 다음 칸으로 이동
    if sudoku[row][col] != 0:
        if col == 8:
            return backtracking(row + 1, 0)
        else:
            return backtracking(row, col + 1)

    # 현재 위치에 숫자를 넣어보면서 가능한지 검사
    for i in range(1, 10):
        if rows[row][i - 1] == 0 and columns[col][i - 1] == 0 and area[(row // 3) * 3 + col // 3][i - 1] == 0:
            # 해당 숫자를 넣어봄
            rows[row][i - 1] = 1
            columns[col][i - 1] = 1
            area[(row // 3) * 3 + col // 3][i - 1] = 1
            sudoku[row][col] = i

            # 다음 칸으로 이동
            if col == 8:
                is_end = backtracking(row + 1, 0)
            else:
                is_end = backtracking(row, col + 1)

            # 해를 찾은 경우 True 반환
            if is_end:
                return True
            else:
                # 현재 숫자로 해를 찾지 못한 경우 초기화
                sudoku[row][col] = 0
                rows[row][i - 1] = 0
                columns[col][i - 1] = 0
                area[(row // 3) * 3 + col // 3][i - 1] = 0
    
    # 가능한 숫자를 모두 시도했지만 해를 찾지 못한 경우 False 반환
    return False

# 초기화
sudoku = [[0] * 9 for _ in range(9)]  # 9x9 스도쿠 초기화
rows = [[0] * 9 for _ in range(9)]    # 행 체크 배열 초기화
columns = [[0] * 9 for _ in range(9)] # 열 체크 배열 초기화
area = [[0] * 9 for _ in range(9)]    # 3x3 영역 체크 배열 초기화

# 입력 받기
for i in range(9):
    s = input()
    for j in range(9):
        if s[j] != '0':
            rows[i][int(s[j]) - 1] = 1
            columns[j][int(s[j]) - 1] = 1
            area[(i // 3) * 3 + j // 3][int(s[j]) - 1] = 1
        sudoku[i][j] = int(s[j])

# 백트래킹 실행
backtracking(0, 0)

# 결과 출력
for i in range(9):
    for j in range(9):
        print(sudoku[i][j], end="")
    print()
