import sys
from functools import cmp_to_key
sys.stdin = open("input.txt", 'r')

N = int(input())
arr = list(map(int, input().split(' ')))

def compare(x, y):
    if int(str(x)+str(y)) > int(str(y)+str(x)):
        return -1
    else:
        return 1

arr.sort(key=cmp_to_key(compare))
ans = int(''.join(map(str, arr)))
print(ans)
