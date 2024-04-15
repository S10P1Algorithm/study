from collections import deque
N = int(input())
arr = [[0]*N for _ in range(N)]
visited = set()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

start = []
end = []
for i in range(N):
    line = input()
    for j in range(N):
        arr[i][j] = line[j]
        if line[j] == "B":
            start.append((i, j))
        if line[j] == "E":
            end.append((i, j))
q = deque()
# (x1, y1, x2, y2, x3, y3)
visited.add((start[0][0], start[0][1], start[1][0], start[1][1], start[2][0], start[2][1]))
start.append(0)
# [(x1, y1), (x2, y2), (x3, y3), 0]
q.append(start)
check = False
res = 0
while q:
    now = q.popleft()
    ax, ay = now[0][0], now[0][1]
    bx, by = now[1][0], now[1][1]
    cx, cy = now[2][0], now[2][1]
    cnt = now[3]

    if (ax, ay) == end[0] and (bx, by) == end[1] and (cx, cy) == end[2]:
        check = True
        res = cnt
        break

    for i in range(4):
        nax = ax + dx[i]
        nay = ay + dy[i]
        nbx = bx + dx[i]
        nby = by + dy[i]
        ncx = cx + dx[i]
        ncy = cy + dy[i]

        # 옮긴 좌표가 격자를 벗어나지 않아야함
        if 0<=nax<N and 0<=nay<N and 0<=nbx<N and 0<=nby<N and 0<=ncx<N and 0<=ncy<N:
            # visited 안에 없으면
            if (nax, nay, nbx, nby, ncx, ncy) not in visited:
                # 옮기려는 곳에 통나무가 없으면
                if arr[nax][nay] != "1" and arr[nbx][nby] != "1" and arr[ncx][ncy] != "1":
                    visited.add ((nax, nay, nbx, nby, ncx, ncy))
                    q.append([(nax, nay), (nbx, nby), (ncx, ncy), cnt + 1])
    # 통나무가 세로일 때 가로로 회전
    if bx - 1 == ax:
        # 돌린 가로가 격자를 벗어나지 않으면
        if 0 <= ay - 1 < N and 0 <= ay + 1 < N and 0 <= by - 1 < N and 0 <= by + 1 < N and 0 <= cy - 1 < N and 0 <= cy + 1 < N:
            # 세로일 때 양 옆 6칸에 통나무가 있으면 안됨
            if arr[ax][ay - 1] != "1" and arr[ax][ay + 1] != "1" and arr[bx][by - 1] != "1" and arr[bx][by + 1] != "1" and arr[cx][cy - 1] != "1" and arr[cx][cy + 1] != "1":
                axx = ax + 1
                ayy = ay - 1
                bxx = bx
                byy = by
                cxx = cx - 1
                cyy = cy + 1
                if 0 <= axx < N and 0 <= ayy < N and 0 <= bxx < N and 0 <= byy < N and 0 <= cxx < N and 0 <= cyy < N:
                    if (axx, ayy, bxx, byy, cxx, cyy) not in visited:
                        if arr[axx][ayy] != "1" and arr[bxx][byy] != "1" and arr[cxx][cyy] != "1":
                            visited.add((axx, ayy, bxx, byy, cxx, cyy))
                            q.append([(axx, ayy), (bxx, byy), (cxx, cyy), cnt + 1])
    # 통나무가 가로일 때 세로로 회전
    else:
        if 0 <= ax - 1 < N and 0 <= ax + 1 < N and 0 <= bx - 1 < N and 0 <= bx + 1 < N and 0 <= cx - 1 < N and 0 <= cx + 1 < N:
            if arr[ax - 1][ay] != "1" and arr[ax + 1][ay] != "1" and arr[bx - 1][by] != "1" and arr[bx + 1][by] != "1" and arr[cx - 1][cy] != "1" and arr[cx + 1][cy] != "1":
                axx = ax - 1
                ayy = ay + 1
                bxx = bx
                byy = by
                cxx = cx + 1
                cyy = cy - 1
                if 0 <= axx < N and 0 <= ayy < N and 0 <= bxx < N and 0 <= byy < N and 0 <= cxx < N and 0 <= cyy < N:
                    if (axx, ayy, bxx, byy, cxx, cyy) not in visited:
                        if arr[axx][ayy] != "1" and arr[bxx][byy] != "1" and arr[cxx][cyy] != "1":
                            visited.add((axx, ayy, bxx, byy, cxx, cyy))
                            q.append([(axx, ayy), (bxx, byy), (cxx, cyy), cnt + 1])

print(res)


# https://kante-dev.tistory.com/entry/BOJ-1938-%ED%86%B5%EB%82%98%EB%AC%B4-%EC%98%AE%EA%B8%B0%EA%B8%B0-Python
