import sys
sys.stdin = open('input.txt', 'r')

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

prefix_sum = [[0] * (M+1) for _ in range(N+1)]
for i in range(N):
    for j in range(M):
        prefix_sum[i+1][j+1] = A[i][j] + prefix_sum[i+1][j] + prefix_sum[i][j+1] - prefix_sum[i][j]

ans = 0

temp_arr = [0] * (N+1)
for i in range(M):
    for j in range(i+1, M+1):
        temp_dict = {}
        for k in range(1, N+1):
            temp_arr[k] = (prefix_sum[k][j] - prefix_sum[k][i]) % K
        for k in range(N+1):
            temp_dict.setdefault(temp_arr[k], 0)
            temp_dict[temp_arr[k]] += 1
        for q, n in temp_dict.items():
            ans += n*(n-1)//2

print(ans)