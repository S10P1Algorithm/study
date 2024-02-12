import sys
from itertools import combinations
from collections import defaultdict
input = sys.stdin.readline

N, target = map(int,input().split())

arr = list(map(int,input().split()))

# 반띵으로 나누기  2^40 을 => 2^21로 줄이기 약 1000 * 1000 = 백만
left = arr[:N//2]
right = arr[N//2:]

# 값을 지정 안 할경우 기본 값은 0, list를 넣으면 빈배열
left_sub = defaultdict(int)
right_sub = defaultdict(int)

# 왼쪽 서브셋 경우의 수 합 저장
for i in range(1, len(left) + 1):
    for j in combinations(left, i):
        tmp = sum(j)
        left_sub[tmp] += 1

# 오른쪽 서브셋 경우의 수 합 저장
for i in range(1, len(right) + 1):
    for j in combinations(right, i):
        tmp = sum(j)
        right_sub[tmp] += 1

# target이 각각 있을때 더해주기
res = left_sub[target] + right_sub[target]

# target = left_sub[?] + right_sub[?] 이다.
for ans in left_sub:
    if target - ans in right_sub:
        res += left_sub[ans] * right_sub[target - ans]

print(res)