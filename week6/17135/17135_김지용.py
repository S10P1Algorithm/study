from collections import deque
from itertools import combinations
import sys

input = sys.stdin.readline

N, M, D = map(int, input().split())

field = deque()


def shoot_range(archer, dist):
    result = []
    for row in range(N):
        for col in range(M):
            if abs(0 - row) + abs(archer - col) < dist:
                result.append((row, col))

    return result


for _ in range(N):
    field.appendleft(list(map(int, input().split())))

max_kill = 0

for archers in combinations(range(M), 3):
    curr_kill = 0
    l = N + 1
    new_field = deque([i.copy() for i in field])

    while new_field:
        l -= 1
        for archer in archers:
            for spot in shoot_range(archer, D):
                spot_row, spot_col = spot
                if spot_row < l and new_field[spot_row][spot_col]:
                    curr_kill += 1
                    new_field[spot_row][spot_col] -= 1

                    break
        new_field.popleft()

    max_kill = max(max_kill, curr_kill)

print(max_kill)
