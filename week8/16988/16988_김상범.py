from collections import deque

N = 0
M = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
badukPlate = [[0] * 20 for _ in range(20)]
visited = [[0] * 20 for _ in range(20)]


def bfs(x, y, whereOneCanPut):
    global visited
    q = deque()
    visited[x][y] = 98
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                if badukPlate[nx][ny] == 2:
                    visited[nx][ny] = 98
                    q.append((nx, ny))
                elif badukPlate[nx][ny] == 0:
                    visited[nx][ny] = 99
                    whereOneCanPut.append((nx, ny))


def bfs2(x, y):
    global visited
    q = deque()
    q.append((x, y))
    cnt = 0
    visited[x][y] = 98
    while q:
        x, y = q.popleft()
        cnt += 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                if badukPlate[nx][ny] == 2:
                    visited[nx][ny] = 98
                    q.append((nx, ny))
                elif badukPlate[nx][ny] == 0:
                    return 0
    return cnt


if __name__ == "__main__":
    with open("16988.txt", "r") as f:
        N, M = map(int, f.readline().split())
        for i in range(N):
            badukPlate[i] = list(map(int, f.readline().split()))

    baduk_set = []
    whereOneCanPut = []
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and badukPlate[i][j] == 2:
                baduk_set.append((i, j))
                bfs(i, j, whereOneCanPut)

    for i in range(N):
        for j in range(M):
            visited[i][j] = 0

    maxAns = 0
    if len(whereOneCanPut) == 1:
        x1, x2 = whereOneCanPut[0]
        badukPlate[x1][x2] = 1
        tmpAns = 0
        for k in range(len(baduk_set)):
            tmpAns += bfs2(baduk_set[k][0], baduk_set[k][1])
        if tmpAns > maxAns:
            maxAns = tmpAns
    else:
        for i in range(len(whereOneCanPut)):
            for j in range(i + 1, len(whereOneCanPut)):
                x1, x2 = whereOneCanPut[i]
                y1, y2 = whereOneCanPut[j]
                tmpAns = 0
                for m in range(N):
                    for n in range(M):
                        visited[m][n] = 0
                badukPlate[x1][x2] = 1
                badukPlate[y1][y2] = 1
                for k in range(len(baduk_set)):
                    tmpAns += bfs2(baduk_set[k][0], baduk_set[k][1])
                if tmpAns > maxAns:
                    maxAns = tmpAns
                badukPlate[x1][x2] = 0
                badukPlate[y1][y2] = 0

    print(maxAns)
