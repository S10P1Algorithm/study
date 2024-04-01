import sys
input = sys.stdin.readline
from functools import cmp_to_key

N = int(input())
arr = list(map(int, input().split()))


def compare(x, y):
    if str(x)+str(y) > str(y)+str(x):
        return -1  # x먼저
    if str(x) + str(y) > str(y) + str(x):
        return 1  # y먼저
    return 0  # 냅두기


arr.sort(key=cmp_to_key(compare))
count = 0
for num in arr:
    if num == 0:
        count += 1

if count == len(arr):
    print(0)
else:
    for num in arr:
        print(num, end='')





# https://brorica.tistory.com/205
# https://steadily-worked.tistory.com/901
# https://velog.io/@heyday_7/python-%EC%A1%B0%EA%B1%B4-%EC%A0%95%EB%A0%AC-%ED%95%98%EA%B8%B0-cmptokey