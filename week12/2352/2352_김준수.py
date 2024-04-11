import sys
input = sys.stdin.readline


def binary_search(target, arr):
    start, end = 0, len(arr)-1
    while start < end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid-1] < target < arr[mid]:
            return mid
        elif target < arr[mid]:
            end = mid - 1
        else: start = mid + 1
    return start


N = int(input())
port = list(map(int, input().split()))

result = [port[0]]
for i in range(1, N):
    target = port[i]
    if result[-1] < target:
        result.append(target)
    else:
        fi = binary_search(target, result)
        result[fi] = target

print(len(result))