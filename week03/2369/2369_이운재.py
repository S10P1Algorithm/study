import sys 
input = sys.stdin.readline

n, m, k = map(int,input().split())

array = []
for _ in range(n):
    array.append(list(map(int,input().split())))

sum_dp = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        sum_dp[i][j] = sum_dp[i][j-1] + sum_dp[i-1][j] - sum_dp[i-1][j-1] + array[i-1][j-1]


print(sum_dp)