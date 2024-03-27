from collections import deque

N, T = map(int, input().split())

field = [tuple(map(int, input())) for _ in range(N)]

dp = [[-1001] * N for _ in range(N)]
reverse_dp = [[-1001] * N for _ in range(N)]

dp[0][0] = field[0][0]
reverse_dp[N - 1][N - 1] = field[N - 1][N - 1]

# (1,1)에서 특정 지점까지의 최대 이익을 dp로 계산

# 극단에 있는 점 미리 설정
for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + field[i][0]
    dp[0][i] = dp[0][i - 1] + field[0][i]

for r in range(1, N):
    for c in range(1, N):
        dp[r][c] = max(dp[r - 1][c], dp[r][c - 1]) + field[r][c]

# 특정 지점에서 최종 도착지(N-1,N-1)까지 최대 이익 계산, (N-1,N-1) 에서 역으로 계산

# 극단에 있는 점 미리 설정
for i in range(N - 2, -1, -1):
    reverse_dp[i][N - 1] = reverse_dp[i + 1][N - 1] + field[i][N - 1]
    reverse_dp[N - 1][i] = reverse_dp[N - 1][i + 1] + field[N - 1][i]

for r in range(N - 2, -1, -1):
    for c in range(N - 2, -1, -1):
        reverse_dp[r][c] = max(reverse_dp[r + 1][c], dp[r][c + 1]) + field[r][c]

# 빠구 안칠 때의 경우를 미리 저장
result = reverse_dp[0][0]

# bfs에 쓸 델타값
delta_r = [0, 1]
delta_c = [1, 0]


# 특정 지점(i, j)을 리턴 되는 지점으로 가정할 때
# T 만큼 거리의 지점을 bfs로 찾아서 거기서 빠꾸 쳤을 때의 최대 이익값을
# 기존의 최대 이익값(result)과 비교하여 계속 업데이트 하는 구조
def find_max_cnt(i, j):
    global result

    # 리턴된 지점에서 도착점까지의 최댓값
    curr_cnt = reverse_dp[i][j]

    q = deque()

    # (행, 열, 거리)
    q.append((i, j, 0))

    # BFS 시작
    while q:
        row, col, cnt = q.popleft()

        # 거리가 T 인 경우
        if cnt == T:
            # 리턴된 지점에서 도착점까지 최대 이익값(curr_cnt)
            # 시작점부터 리턴 하는 지점까지의 최대 이익값(dp[i][j])
            result = max(result, curr_cnt + dp[i][j])

        # 거리가 T까지 도달 하지 못한 경우
        # 갈 수 있는 지점 큐에 계속 추가
        else:
            for k in range(2):
                nxt_row = row + delta_r[k]
                nxt_col = col + delta_c[k]
                if 0 <= nxt_row < N and 0 <= nxt_col < N:
                    q.append((nxt_row, nxt_col, cnt + 1))


for i in range(N):
    for j in range(N):
        find_max_cnt(i, j)

print(result)
