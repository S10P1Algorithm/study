import sys

input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

cnt = 0


# 병합 정렬(merge sort)를 사용한다.
def merge(input_arr, start, mid, end):
    global cnt
    left_arr = input_arr[start:mid + 1]
    right_arr = input_arr[mid + 1:end + 1]

    left_len = len(left_arr)
    right_len = len(right_arr)

    left_index = 0
    right_index = 0
    curr_index = start

    while left_index < left_len and right_index < right_len:
        if left_arr[left_index] <= right_arr[right_index]:
            input_arr[curr_index] = left_arr[left_index]
            left_index += 1
        else:
            input_arr[curr_index] = right_arr[right_index]

            # 왼쪽의 숫자들이 뒤(오른쪽)로 가야할 때 가야되는 길이만큼 cnt에 더한다.
            cnt += (left_len - left_index)
            right_index += 1

        curr_index += 1

    while left_index < left_len:
        input_arr[curr_index] = left_arr[left_index]
        left_index += 1
        curr_index += 1

    while right_index < right_len:
        input_arr[curr_index] = right_arr[right_index]
        right_index += 1
        curr_index += 1


def merge_sort(input_arr, start, end):
    if start >= end:
        return
    mid = (start + end) // 2
    merge_sort(input_arr, start, mid)
    merge_sort(input_arr, mid + 1, end)
    merge(input_arr, start, mid, end)


merge_sort(arr, 0, len(arr))

print(cnt)
