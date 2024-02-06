import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

total_C = sum(C)

dp = [[0]*(total_C + 1) for _ in range(N)]

for i in range(total_C+1):
    if A[0] <= M and i >= C[0]:
        dp[0][i] = A[0]


for i in range(1, N):
    for j in range(total_C+1):
        if j < C[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-C[i]] + A[i], dp[i-1][j])

for ans in range(total_C+1):
    if dp[N-1][ans] >= M:
        break

print(ans)