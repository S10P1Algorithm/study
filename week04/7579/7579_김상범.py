import sys

DPpann = [[0] * 10000000 for _ in range(100)]
benefit = [0] * 100
cost = [0] * 100
maxVal = 200000000

def dp(n, M):
    if M <= 0:
        return 0
    if n < 0 and M:
        return maxVal
    if DPpann[n][M]:
        return DPpann[n][M]
    tmp1 = dp(n - 1, M - benefit[n]) + cost[n]
    tmp2 = dp(n - 1, M)
    DPpann[n][M] = min(tmp1, tmp2)
    return DPpann[n][M]

# 입력 파일에서 데이터를 읽기 위해 파일 핸들을 엽니다.
with open("7579.txt", 'r') as file:
    lines = file.readlines()
    N, M = map(int, lines[0].split())
    benefit = list(map(int, lines[1].split()))
    cost = list(map(int, lines[2].split()))

print(dp(N - 1, M))
