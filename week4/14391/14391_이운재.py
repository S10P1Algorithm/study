# N, M = map(int,input().split())
#
# max_v = 0
#
# arr = []
#
# for i in range(N):
#     arr.append(list(input()))
#
# res1 = 0
# for i in range(N):
#     tmp = ''
#     for j in range(M):
#         tmp += arr[i][j]
#     res1 += int(tmp)
# res2 = 0
# for j in range(M):
#     tmp2 = ''
#     for i in range(N):
#         tmp2 += arr[i][j]
#     res2 += int(tmp2)
#
# print(max(res1, res2))

# 당연히 틀렷을거 같았는데, 근데 최고 자리수만 하면 되는거 아닌가 ?

from itertools import product

N, M = map(int,input().split())
arr = []

for i in range(N):
    arr.append(list(input()))

# 0,1로 이루어진 모든 경우의 종이 조각 수
# ex) 2*3의 사각형이라면 (0,0,0,0,0,0) 이면 가로 종이 조각이 2개 (0,0,1,0,0,1) 이면 가로조각 2개 세로조각 1개
squares = product(range(2), repeat=N*M)

max_v = 0

for square in squares:
    tmp = 0
    # 가로
    for i in range(N):
        sum1 = 0
        for j in range(M):
            # ex) 2*3의 행렬 이라면 (0, 0, 1 / 1, 0, 0) 로 쪼개짐
            row = i*M + j
            if square[row] == 0:
                # 숫자 범위가 0 <= number <= 9 이기 때문에 문제 조건에 따라 왼-> 오, 위-> 아래 로 읽기 때문에 10 곱해서 자리수를 완성해준다.
                sum1 = 10 * sum1 + int(arr[i][j])
            else:
                tmp += sum1
                sum1 = 0
        # ex) 2*3 행렬인데 (1,1,0 / 1,1,0) 인 경우  즉 , j = M 일 경우를 대비해서 반영
        if sum1 != 0:
            tmp += sum1
    # 세로
    for i in range(M):
        sum2 = 0
        for j in range(N):
            col = i + j*M
            if square[col] == 1:
                sum2 = 10 * sum2 + int(arr[j][i])
            else:
                tmp += sum2
                sum2 = 0
        if sum2 != 0:
            tmp += sum2
    max_v = max(max_v, tmp)

print(max_v)

# 비트마스킹의 << 을 쓰는 방법이 아닌 모든 경우의 수를 써서 하는 접근이 새로 알게된 방법이었다.