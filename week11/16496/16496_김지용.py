import sys

input = sys.stdin.readline

N = int(input())

arr = list(input().strip().split())


def compare(str1, str2):
    if str1 == str2:
        return True

    l1 = len(str1)
    l2 = len(str2)

    idx = 0

    while idx < l1 and idx < l2:
        if int(str1[idx]) > int(str2[idx]):
            return True
        elif int(str1[idx]) < int(str2[idx]):
            return False
        else:
            idx += 1

    if l1 > l2:
        if compare(str1[idx:], str2):
            return True
        else:
            return False
    elif l1 < l2:
        if compare(str1, str2[idx:]):
            return True
        else:
            return False


def merge(start, mid, end):
    global arr
    left = arr[start:mid + 1]
    right = arr[mid + 1:end + 1]

    left_idx = 0
    right_idx = 0
    curr_idx = start

    ll = len(left)
    rl = len(right)

    while left_idx < ll and right_idx < rl:
        le = left[left_idx]
        re = right[right_idx]
        if compare(le, re):
            arr[curr_idx] = le
            curr_idx += 1
            left_idx += 1
        else:
            arr[curr_idx] = re
            curr_idx += 1
            right_idx += 1

    while left_idx < ll:
        arr[curr_idx] = left[left_idx]
        curr_idx += 1
        left_idx += 1

    while right_idx < rl:
        arr[curr_idx] = right[right_idx]
        curr_idx += 1
        right_idx += 1


def merge_sort(start, end):
    if start >= end:
        return
    mid = (start + end) // 2
    merge_sort(start, mid)
    merge_sort(mid + 1, end)
    merge(start, mid, end)


merge_sort(0, N - 1)

print(int("".join(arr)))
