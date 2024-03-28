from copy import deepcopy


def play(enemies, archers, kill):
    while len(enemies) > 0:
        enemy = deepcopy(enemies)
        kill_set = set()
        for a in archers:
            min_d = D+1
            target = 0
            for e in enemy:
                d = abs(a[0] - e[0]) + abs(a[1] - e[1])
                if min_d > d:
                    min_d = d
                    target = e
            if target != 0:
                kill_set.add(target)

        enemies = []
        for e in enemy:
            if e in kill_set:
                kill += 1
                continue
            ni = e[0] + 1
            if ni < N:
                enemies.append((ni, e[1]))
    return kill


N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
enemies = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            enemies.append((i, j))
enemies.sort(key=lambda e: e[1])

max_kill = 0
for i in range(0, M-2):
    for j in range(i+1, M-1):
        for k in range(j+1, M):
            a1 = [N, i]
            a2 = [N, j]
            a3 = [N, k]
            archer = [a1, a2, a3]
            kill = play(enemies, archer, 0)
            if max_kill < kill:
                max_kill = kill
print(max_kill)
