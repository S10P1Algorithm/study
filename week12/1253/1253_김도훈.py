import sys
sys.stdin = open('input.txt', 'r')
N = int(input())

arr = list(map(int, input().split()))
arr.sort()

ans = 0
for i in range(N):
    start = 0
    end = N-1
    while start < end:
        if arr[start] + arr[end] == arr[i]:
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                ans += 1
                break
        elif arr[start] + arr[end] < arr[i]:
            start += 1
        else:
            end -= 1

print(ans)