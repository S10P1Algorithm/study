import sys
input = sys.stdin.readline
from itertools import combinations

N, C = map(int, input().split())
w_list = list(map(int, input().split()))

l_list = w_list[:N//2]
r_list = w_list[N//2:]

l_subsum = []
r_subsum = []

for i in range(len(l_list) + 1):
    l_comb = combinations(l_list, i)
    for comb in l_comb:
        l_subsum.append(sum(comb))

for j in range(len(r_list) + 1):
    r_comb = combinations(r_list, j)
    for comb in r_comb:
        r_subsum.append(sum(comb))

r_subsum.sort()
cnt = 0

for l_sum in l_subsum:

    if l_sum > C:
        continue

    start = 0
    end = len(r_subsum) - 1

    while start <= end:
        mid = (start + end) // 2

        if r_subsum[mid] + l_sum > C:
            end = mid - 1

        else:
            start = mid + 1

    cnt += end + 1

print(cnt)

# https://seongonion.tistory.com/105
