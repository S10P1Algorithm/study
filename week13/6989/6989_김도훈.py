import sys
# sys.stdin = open("input.txt", 'r')

# 1<=N<=150, 1<=score[i]<=100, 1<=K<=2*1e9
N = int(input())
score = list(map(int, input().split()))
K = int(input())

# dp 안에 들어갈 최대 수 : 1~150 까지의 합 * 100 = 1132500, (1<<1132501)-1
dp = [1] * N

init_bit = 1<<score[0]
init_score = score[0]
dp[0] |= init_bit
for i in range(1, N):
    init_score += score[i]
    init_bit = init_bit<<init_score
    dp[i] |= init_bit
if N < 2:
    pass
else:
    sec_bit = 1<<score[1]
    sec_score = score[1]
    dp[1] |= dp[0]
    dp[1] |= sec_bit
    for i in range(2, N):
        sec_score += score[i]
        sec_bit = sec_bit << sec_score
        dp[i] |= sec_bit
if N < 3:
    pass
else:
    for i in range(2, N-1):
        temp_bit = dp[i-2]<<score[i]
        dp[i] |= dp[i-1]
        dp[i] |= temp_bit
        curr_score = score[i]
        for j in range(i + 1, N):
            curr_score += score[j]
            temp_bit = temp_bit << curr_score
            dp[j] |= temp_bit

    final_bit = dp[N-3]<<score[N-1]
    dp[N-1] |= final_bit
    dp[N-1] |= dp[N-2]
ans = 0
if K >= 1132500:
    print(K)
else:
    for i in range(K, 1132500):
        if not(dp[N-1] & 1<<i):
            ans = i
            break
    # debug_string = bin(dp[N-1])
    # for c, idx in enumerate(debug_string):
    #     print("index: ", idx, ", sum: ", 186-c)
    # print(bin(dp[N-1]))

    print(ans)
