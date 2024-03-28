import sys
input = sys.stdin.readline

N, S = map(int, input().split())

arr = list(map(int, input().split()))

def join_arr(a, b):
    result = []

    for i in a:
        for j in b:
            result.append(i + j)

    result.extend(a)
    result.extend(b)

    return result


def binary_search(arr, start, end):
    if start >= end:
        return [arr[start]]
    mid = (start + end) // 2
    left_arr = binary_search(arr, start, mid)
    right_arr = binary_search(arr, mid + 1, end)
    return join_arr(left_arr, right_arr)


print(binary_search(arr,0, N-1).count(S))