import sys
sys.stdin = open("input.txt", "r")
input = lambda: sys.stdin.readline().rstrip()
T = int(input())
for _ in range(T):
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N == 1:
        if A[0] + B[0] <= W:
            print(1)
        else:
            print(2)
        continue

    dp = [[[0]*4 for _ in range(4)] for _ in range(N)]


    # 00, 01, 10, 11
    dp[1][0][0] = 0
    dp[1][0][1] = 1
    dp[1][0][2] = 1
    if A[1] + B[1] <= W:
        dp[1][0][3] = 1
    else:
        dp[1][0][3] = 2
    
    dp[1][1][0] = 1
    if A[0] + A[1] <= W:
        dp[1][1][1] = 1
        dp[1][1][3] = 2
    else:
        dp[1][1][1] = 2
        dp[1][1][3] = 3
    dp[1][1][2] = 2
    if A[1] + B[1] <= W:
        dp[1][1][3] = 2

    dp[1][2][0] = 1
    dp[1][2][1] = 2
    if B[0] + B[1] <= W:
        dp[1][2][2] = 1
        dp[1][2][3] = 2
    else:
        dp[1][2][2] = 2
        dp[1][2][3] = 3
    if A[1] + B[1] <= W:
        dp[1][2][3] = 2

    if A[0] + B[0] <= W:
        dp[1][3][0] = 1
        dp[1][3][1] = 2
        dp[1][3][2] = 2
        if A[1] + B[1] <= W:
            dp[1][3][3] = 2
        else:
            if A[0] + A[1] <= W and B[0] + B[1] <= W:
                dp[1][3][3] = 2
            else:
                dp[1][3][3] = 3
    else:
        dp[1][3][0] = 2
        if A[0] + A[1] <= W:
            dp[1][3][1] = 2
        else:
            dp[1][3][1] = 3
        if B[0] + B[1] <= W:
            dp[1][3][2] = 2
        else:
            dp[1][3][2] = 3
        
        if A[0] + A[1] <= W and B[0] + B[1] <= W:
            dp[1][3][3] = 2
        else:
            if A[1] + B[1] <= W:
                dp[1][3][3] = 3
            else:
                dp[1][3][3] = min(dp[1][3][1], dp[1][3][2]) + 1
    if N == 2:
        print(dp[1][3][3])
        continue



    for i in range(2, N):
        for init_state in range(4):
            dp[i][init_state][0] = dp[i-1][init_state][3]
            if A[i-1] + A[i] <= W:
                dp[i][init_state][1] = dp[i-1][init_state][2] + 1
            else:
                dp[i][init_state][1] = dp[i-1][init_state][3] + 1
            if B[i-1] + B[i] <= W:
                dp[i][init_state][2] = dp[i-1][init_state][1] + 1
            else:
                dp[i][init_state][2] = dp[i-1][init_state][3] + 1

            dp[i][init_state][3] = min(dp[i][init_state][1], dp[i][init_state][2]) + 1
            if A[i] + B[i] <= W:
                dp[i][init_state][3] = min(dp[i-1][init_state][3] + 1, dp[i][init_state][3])
            else:
                dp[i][init_state][3] = min(dp[i-1][init_state][3] + 2, dp[i][init_state][3])
            if A[i-1] + A[i] <= W and B[i-1] + B[i] <= W:
                dp[i][init_state][3] = min(dp[i][init_state][3], dp[i-1][init_state][0] + 2)

    ans = dp[N-1][3][3]
    if A[0] + A[N-1] <= W:
        ans = min(ans, dp[N-1][2][2] + 1)
        if B[0] + B[N-1] <= W:
            ans = min(ans, dp[N-1][0][0] + 2)
    if B[0] + B[N-1] <= W:
        ans = min(ans, dp[N-1][1][1] + 1)

    print(ans)
        