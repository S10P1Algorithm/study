import sys
sys.setrecursionlimit(200000)


'''
# 입력

n * n 의 대나무 숲이 있고 

# 과정

다먹으면 이동하는 룰,다음에 이동하는 지역은 반드시 지금 지역보다 대나무가 많다

# 출력

판다가 이동할 수 있는 칸의 최대값

### 그냥 전부 계산

---

각 행마다 dfs해서 25000 * 25000 ⇒ 최대 625억

그런데 각 dfs마다  어떤 한 칸에서 이동할 수있는 최대의 방향수가 정해졌다면 그건 이전 결과 값에 상관 없이 같다 

4개이며 길이 탐색의 가장 긴 경우의 수는 25000개

이미 한번 갈 수 있는 최대 길이가 정해진 곳은 다시 참조했을때 이전 상황과 상관없이 같은 결과를 낸다 ⇒ 저장해도 문제가 없다 .

dfs의 총 횟수는 25000개로 정해져 있고 한 dfs가 길 수록 이후 dfs의 횟수가 적어진다

(25000 - x)(x) = 1억 살짝넘음


'''

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
# dx, dy, dp 설정

# dp 함수
def dfs(x, y):
    # 방문한적있나?
    if visited[x][y]:
        # yes일시 저장 값리턴
        return visited[x][y]
    # no일경우 최소 결과값 설정
    ret = 1
    # 4방향 이동
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        # 범위안에 있고 그쪽이 더 큰가?
        if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] > matrix[x][y]:
            # yes 일시 저장 돼 있는가? 
            if visited[nx][ny]:
                # yes 일시 리턴값은 기존의 max값과 저장된 값 + 1
                ret = max(ret, visited[nx][ny] + 1)
            else:
                # no 일시 리턴값은 기존의 max값과 새 좌표의 dp 값 + 1
                ret = max(ret, dfs(nx, ny) + 1)

    visited[x][y] = ret
    # 값 저장
    return ret


ans = 1
for i in range(N):
    for j in range(N):
        ans = max(ans, dfs(i, j))

print(ans)