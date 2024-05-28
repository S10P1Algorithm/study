import sys
import copy

N = int(input())
Mod = 10**9 + 7


V = 14
G = [[1, 2, 4], [2], [1, 3], [4], [5, 12], [6], [7, 13], [8], [9, 10], [10], [11], [0], [0, 5, 6, 10, 13], [8, 10]]
A, B = 0, 13

dist = [[15]*14 for _ in range(14)]

# 초기화
for i in range(V):
    dist[i][i] = 0
    for j in G[i]:
        dist[i][j] = 1
# Floyd-warshall
for k in range(V):
    for i in range(V):
        for j in range(V):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

bit_N = []
for i in range(30):
    if N & 1<<i:
        bit_N.append(i)
max_bit = bit_N[-1]

# 2**30 = 1,073,741,824
dp = [[[[[0]*14 for _ in range(14)] for _ in range(14)] for _ in range(14)] for _ in range(max_bit+1)]

# initialize
for i in range(V):
    for j in range(V):
        for n_i in G[i]:
            for n_j in G[j]:
                if dist[n_i][n_j] >= 3 and dist[n_j][n_i] >= 3:
                    dp[0][i][j][n_i][n_j] = 1

for k in range(max_bit):
    for i in range(V):
        for j in range(V):
            if dist[i][j] < 3 or dist[j][i] < 3:
                continue
            for n_i in range(V):
                for n_j in range(V):
                    if dist[n_i][n_j] < 3 or dist[n_j][n_i] < 3:
                        continue
                    for mid_i in range(V):
                        for mid_j in range(V):
                            if dist[mid_i][mid_j] < 3 or dist[mid_j][mid_i] < 3:
                                continue
                            dp[k+1][i][j][n_i][n_j] += (dp[k][i][j][mid_i][mid_j]*dp[k][mid_i][mid_j][n_i][n_j])
                            dp[k+1][i][j][n_i][n_j] %= Mod

ans = copy.deepcopy(dp[bit_N[0]])
if len(bit_N) > 1:
    for k in range(1, len(bit_N)):
        prev_ans = copy.deepcopy(ans)
        for i in range(V):
            for j in range(V):
                for n_i in range(V):
                    for n_j in range(V):
                        ans[i][j][n_i][n_j] = 0
        bit = bit_N[k]
        for i in range(V):
            for j in range(V):
                if dist[i][j] < 3 or dist[j][i] < 3:
                    continue
                for n_i in range(V):
                    for n_j in range(V):
                        if dist[n_i][n_j] < 3 or dist[n_j][n_i] < 3:
                            continue
                        for mid_i in range(V):
                            for mid_j in range(V):
                                if dist[mid_i][mid_j] < 3 or dist[mid_j][mid_i] < 3:
                                    continue
                                ans[i][j][n_i][n_j] += (prev_ans[i][j][mid_i][mid_j]*dp[bit][mid_i][mid_j][n_i][n_j])
                                ans[i][j][n_i][n_j] %= Mod


answer = 0
for i in range(V):
    for j in range(V):
        answer += ans[A][B][i][j]
        answer %= Mod
print(answer)