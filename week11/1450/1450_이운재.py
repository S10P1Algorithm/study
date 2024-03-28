# 5주차에 했던 1208번 문제와 99.9% 유사함

import sys
from itertools import combinations
input= sys.stdin.readline

N, C = map(int,input().split())

arr = list(map(int,input().split()))

# 반 쪼개주고
left = arr[:N//2]
right = arr[N//2:]

# 조합의따른 무게의 합을 넣어줄 미니배열 만들어주고
leftsum = []
rightsum = []

# 0개씩 조합했을때 무게, 1개씩 조합했을때 무게 ..... N개씩 조합했을떄 무게구해서 넣어줌 N이 최대 30이고 조합이라 문제없음. 순열이면 문제 있을지도 ?
for i in range(len(left)+1):
    tmp = combinations(left,i)

    for j in tmp:
        leftsum.append(sum(j))

for i in range(len(right) + 1):
    tmp = combinations(right, i)

    for j in tmp:
        rightsum.append(sum(j))

# 이분탐색의 전제는 뭐다 ? 탐색 돌릴 것이 정렬이 되어있어야 한다.
leftsum.sort()

res = 0

# 오른쪽 미니배열을 하나씩 탐색해서  왼쪽미니배열을 이분탐색을 돌려주는데 end만 찾아주면 end까지 다 가방에 들어간다는 소리
for k in rightsum:

    if k > C:
        continue

    start = 0
    end = len(leftsum)-1

    while start <= end:

        mid = (start+end) // 2

        if leftsum[mid] + k > C:
            end = mid - 1
        else:
            start = mid + 1
    # 이분탐색이 끝나면 end가 정해진다. 근데 1 더해주자
    res += end + 1

print(res)
