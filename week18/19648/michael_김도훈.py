import sys
sys.stdin = open("input.txt", "r")
V = 14
G = [(1, 2, 4), (2,), (1, 3), (4,), (5, 12), (6,), (7, 13), (8,), (9, 10), (10,), (11,), (0,), (0, 5, 6, 10, 13), (8, 10)]
A, B = 0, 1
Mod = 10**9 + 7

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

pair = []
for i in range(V):
    for j in range(V):
        if dist[i][j] >=3 and dist[j][i] >= 3:
            pair.append((i, j))

N = len(pair)

temp = [[0]*N for _ in range(N)]
ans_arr = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            ans_arr[i][j] = 1
        if pair[j][0] in G[pair[i][0]] and pair[j][1] in G[pair[i][1]]:
            temp[i][j] = 1

t = int(input())
for k in range(30):
    if t & 1<<k:
        temp_ans = [[0] *N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                sum = 0
                for mid in range(N):
                    sum += ans_arr[i][mid] * temp[mid][j]
                    sum %= Mod
                temp_ans[i][j] = sum
        temp_ans, ans_arr = ans_arr, temp_ans

    current = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            sum = 0
            for mid in range(N):
                sum += temp[i][mid] * temp[mid][j] # numpy 쓰면 빠르려나?
                sum %= Mod
            current[i][j] = sum
    temp, current = current, temp

ans = 0
for j in range(N):
    ans += ans_arr[4][j]
    ans %= Mod
print(ans)