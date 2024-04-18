import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):

    N = int(input())

    arr = []
    for i in range(N):
        arr.append(input().rstrip())

    arr.sort()
    # print(arr)
    flag = False
    for i in range(N-1):
        if arr[i] == arr[i+1][:len(arr[i])]:
            flag = True
            break

    if flag:
        print('NO')
    else:
        print('YES')

