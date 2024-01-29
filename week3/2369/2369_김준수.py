import sys
input = sys.stdin.readline

def count_submatrices(N, M, K, matrix):
    count = 0

    # 각 열의 누적 합 계산
    for i in range(N):
        for j in range(1, M):
            matrix[i][j] += matrix[i][j - 1]

    # 부분행렬의 합을 계산하고, 나누어떨어지는 경우 카운트
    for i in range(M):
        for j in range(i, M):
            prefix_sum = [0]
            for k in range(N):
                prefix_sum.append(prefix_sum[-1] + matrix[k][j] - (matrix[k][i - 1] if i > 0 else 0))
            # 부분행렬의 합이 K로 나누어떨어지는 경우 카운트
            for p in range(N):
                for q in range(p, N):
                    if (prefix_sum[q + 1] - prefix_sum[p]) % K == 0:
                        count += 1

    return count

# 입력 처리
N, M, K = map(int, input().split())
matrix = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

# 부분행렬의 개수 계산
result = count_submatrices(N, M, K, matrix)
print(result)
