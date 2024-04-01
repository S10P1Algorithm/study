N, C = map(int, input().split())
arr = list(map(int, input().split()))

left_arr = arr[:N // 2]
right_arr = arr[N // 2:]

ll = len(left_arr)
rl = len(right_arr)

left_sum = []
right_sum = []

left_sum.append(0)
right_sum.append(0)


def l_bt(weight, idx):
    global C, left_arr, ll, left_sum
    if idx == ll - 1:
        return
    for i in range(idx + 1, ll):
        curr = left_arr[i]
        if weight + curr <= C:
            left_sum.append(weight + curr)
            l_bt(weight + curr, i)


def r_bt(weight, idx):
    global C, right_arr, rl, right_sum
    if idx == rl - 1:
        return
    for i in range(idx + 1, rl):
        curr = right_arr[i]
        if weight + curr <= C:
            right_sum.append(weight + curr)
            r_bt(weight + curr, i)


l_bt(0, -1)
r_bt(0, -1)

right_sum.sort()

cnt = 0


def binsearch(target, start, end):
    global right_sum
    while start < end:
        mid = (start + end) // 2
        curr = right_sum[mid]
        if target >= curr:
            start = mid + 1
        else:
            end = mid
    return end


for k in left_sum:
    cnt += binsearch(C - k, 0, len(right_sum))

print(cnt)
