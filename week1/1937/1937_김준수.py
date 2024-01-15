# NxN 대나무 숲
# 상/하/좌/우 이동
# 새로운 위치는 이전 위치보다 대나무의 갯수가 더 많아야 한다.
# 판다가 최대한 많은 칸을 방문할 수 있는 시작 위치와 이동 경로
# 1 <= N <= 500
# 대나무 갯수 <= 1000000
# 판다의 최대 이동 횟수 출력
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(i, j):
    if dp[i][j] == 0:
        dp[i][j] = 1

        for di, dj in delta:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                if forest[ni][nj] > forest[i][j]:
                    dp[i][j] = max(dp[i][j], dfs(ni, nj) + 1)

    return dp[i][j]


N = int(input())
forest = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
max_move = 0

for i in range(N):
    for j in range(N):
        max_move = max(max_move, dfs(i, j))

print(max_move)
