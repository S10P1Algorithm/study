import sys
input = sys.stdin.readline

a = input().strip()
bomb = input().strip()

bomb_end = bomb[-1]
bomb_len = len(bomb)

a_len = len(a)

b = list(bomb)

arr = []

for i in range(a_len):
    curr = a[i]
    arr.append(curr)
    if curr == bomb_end and\
            len(arr) >= bomb_len and\
            arr[-bomb_len:] == b:
        for _ in range(bomb_len):
            arr.pop()

if arr:
    print(''.join(arr))
else:
    print('FRULA')
