import sys
sys.stdin = open("input.txt", 'r')

N = int(input())
arr = list(list(map(lambda c: ord(c) - ord('A'), input())) for _ in range(N))
dp = [[0] * (1<<N) for _ in range(N)]

cost = [[100, 70, 40, 0, 0, 0],
        [70, 50, 30, 0, 0, 0],
        [40, 30, 20, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
        ]

# dp 초기화
# 0번째 행
for j in range(1, N):
    for curr_bit in range(1<<N):
        if (not (curr_bit & 1<<j)) and (not (curr_bit & 1<<(j-1))):
            dp[0][(curr_bit | 1<<j) | 1<<(j-1)] = max(dp[0][curr_bit | 1<<j], dp[0][curr_bit] + cost[arr[0][j]][arr[0][j-1]])



# i번째 행
for i in range(1, N):
    # j번째 열 킬지 말지
    prev_max = 0
    for prev_bit in range(1<<N):
        prev_max = max(prev_max, dp[i-1][prev_bit])
    dp[i][0] = prev_max

    for curr_bit in range(1<<N):
        # 킬 수 있는 경우 - 세로
        for prev_bit in range(1<<N):
            temp = dp[i-1][prev_bit]
            for j in range(N):
                if (curr_bit & 1<<j):
                    if (prev_bit & 1<<j):
                        break
                    else:
                        temp += cost[arr[i][j]][arr[i-1][j]]
            else:
                dp[i][curr_bit] = max(dp[i][curr_bit], temp)      
            

    # 킬 수 있는 경우 - 가로
    for curr_bit in range(1<<N):
        for j in range(1, N):
            if not (curr_bit & 1<<j) and not (curr_bit & 1<<(j-1)):
                new_bit = curr_bit | 1<<j | 1<<(j-1)
                dp[i][new_bit] = max(dp[i][new_bit], dp[i][curr_bit] + cost[arr[i][j]][arr[i][j-1]])
        

ans = 0
for curr_bit in range(1<<N):
    ans = max(ans, dp[N-1][curr_bit])


# for i in range(N):
#     print(i+1,"번째 dp:", end="")
#     for idx, elem in enumerate(dp[i]):
#         print([elem, format(idx, '05b')], end=", ")
#     print()
#     print("=================")

print(ans)