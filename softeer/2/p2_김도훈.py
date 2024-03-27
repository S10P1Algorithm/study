import sys
N, T = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

# 예외처리 빠져있음
# 시간여행으로 돌아왔을때의 최대 Benefit
max_timeB = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        dp_small = [[-5001]*(T+1) for _ in range(T+1)]
        dp_small[0][0] = arr[i][j]
        # dp, row+col ==T인 dp_small값중 최대 local_max로
        local_max = -5001
        for row in range(T):
            for col in range(T):
                dp_small[row][col] = max(dp_small[row-1][col], dp_small[row][col-1]) + arr[i+row][j+col]
                if row + col == T:
                    local_max = max(local_max, dp_small[row][col])
        

        max_timeB[i][j] = local_max

# dp[i][j] = [시간여행 한번도 쓴적 없는 최대B, 시간여행 한번 쓴 최대B]
dp = [[0, 0]*N for _ in range(N)]
dp[0][0][0] = arr[0][0]
dp[0][0][1] = arr[0][0] + max_timeB[0][0]
for i in range(N):
    for j in range(N):
        dp[i][j][0] = max(dp[i-1][j][0], dp[i][j-1][0]) + arr[i][j]
        dp[i][j][1] = max(dp[i][j][0]+max_timeB[i][j], dp[i-1][j][1] + arr[i][j], dp[i][j-1][1] + arr[i][j])

ans = max(dp[i][j][0], dp[i][j][1])