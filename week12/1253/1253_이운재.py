import sys

input = sys.stdin.readline

N = int(input())

arr = list(map(int,input().split()))
arr.sort()

res = 0
for i in range(N):

    start = 0
    end = N-1
    while start < end:

        if arr[start] + arr[end] == arr[i]:
            if start != i and end != i:
                res += 1
                break
            elif start == i:
                start += 1
            elif end == i:
                end -= 1
        elif arr[start] + arr[end] < arr[i]:
            start += 1
        else:
            end -= 1
print(res)




