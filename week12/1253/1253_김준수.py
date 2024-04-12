import sys
input = sys.stdin.readline


N = int(input())
numbers = list(map(int, input().split()))


def binary_search(idx, arr):
    global cnt
    start, end = 0, len(arr)-1
    while start < end:
        if arr[start] + arr[end] == arr[idx]:
            if start == idx:
                start += 1
            elif end == idx:
                end -= 1
            else:
                cnt += 1
                break
        elif arr[start] + arr[end] > arr[idx]:
            end -= 1
        else:
            start += 1


numbers.sort()
cnt = 0
for i in range(0, len(numbers)):
    binary_search(i, numbers)

print(cnt)
