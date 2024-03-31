# import sys   # 88% 까지 맞움
#
# input = sys.stdin.readline
#
# N = int(input())
#
# arr = input().split()
#
# a = max(map(lambda x: len(x),arr))
#
# arr.sort(key=lambda x: -int(x.ljust(a,'0')))
#
# res = int(''.join(arr))
# if res > 0:
#     print(res)
# else:
#     print(0)
#
#
#

import sys

input = sys.stdin.readline

# 입력값
# 5
# 3 30 34 5 9
N = int(input())

arr = list(input().split())

# [1,2,2,1,1] 중 큰값
a = max(map(lambda x: len(x), arr))

# ljust란 자릿수 정렬 예를 들어 81, 803 을 자릿수 정렬 하면 803의 길이는 3이니 3자리 맞춰 정렬하면 810 803이 되어 81,803 정렬이됨
arr.sort(key=lambda x: -int(x.ljust(a, '0')))

res = ''
print(arr)
# 이거 왜함 ? -> 1, 10 ,100 이 자릿수 정렬상 똑같은 위치에 생김 그래서 110100을 기대했으나, 100101, 100110 등 입력값에 따라 다르게 나옴
# 그래서앞 주석 적다가 버그발견
for i in arr:
    res = max(i +res, res + i)

if int(res) > 0:
    print(res)
else:
    print(0)

# 이거 왜맞음 ...?

