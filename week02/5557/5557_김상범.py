# 주어진 숫자들을 이용하여 올바른 등식을 만들 수 있는 경우의 수를 계산하는 함수
def calculate_ways_to_make_equation(TABLE):
    N = len(TABLE)
    VAL = [[0] * (N + 1) for _ in range(21)]  # DP 배열 초기화
    VAL[TABLE[0]][1] = 1

    # DP를 이용하여 올바른 등식의 경우의 수 계산
    for i in range(1, N - 1):
        for j in range(21):
            # 값이 0에서 20 사이에 있을때만
            if 0 <= j + TABLE[i] <= 20:
                VAL[j + TABLE[i]][i + 1] += VAL[j][i]
            if 0 <= j - TABLE[i] <= 20:
                VAL[j - TABLE[i]][i + 1] += VAL[j][i]
    # 테이블 마지막 요소의 값이 N번째까지 수식들에서 몇개나 이용되었는지를 확인
    return VAL[TABLE[N - 1]][N - 1]

# 입력 받고 결과 출력
N = int(input())
TABLE = list(map(int, input().split()))
result = calculate_ways_to_make_equation(TABLE)
print(result)
