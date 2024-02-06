def bitmask():
    global max_answer
    # 비트마스크로 2^(N*M)의 경우의 수를 따짐
    # 2(가로 or 세로)^N*M(행*열 = 총 갯수)
    for i in range(1 << N * M):
        total = 0
        # 가로 합 계산
        # 행으로 순회
        for row in range(N):
            rowsum = 0
            for col in range(M):
                # idx는 이차원 배열을 일렬로 늘렸을 때의 인덱스가 어디인지 의미
                idx = row * M + col
                # 가로일 때
                if i & (1 << idx) != 0:
                    rowsum = rowsum * 10 + arr[row][col]
                # 세로일 때, 앞에서 나온 수를 total에 더하고 rowsum 초기화
                else:
                    total += rowsum
                    rowsum = 0
            total += rowsum
        # 세로 합 계산
        # 열로 순회
        for col in range(M):
            colsum = 0
            for row in range(N):
                # idx는 이차원 배열을 일렬로 늘렸을 때의 인덱스가 어디인지 의미
                idx = row * M + col
                # 세로일 때
                if i & (1 << idx) == 0:
                    colsum = colsum * 10 + arr[row][col]
                # 가로일 때, 앞에서 나온 수를 total에 더하고 colsum 초기화
                else:
                    total += colsum
                    colsum = 0
            total += colsum
        max_answer = max(max_answer, total)


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
# 종이는 가로 / 세로 -> 비트마스킹
max_answer = 0
bitmask()
print(max_answer)

# https://vixxcode.tistory.com/23
# https://thought-process-ing.tistory.com/108
