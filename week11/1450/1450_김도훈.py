import sys
sys.stdin = open("input.txt", 'r')
N, C = map(int, input().split(' '))

arr = list(map(int, input().split(' ')))

def dnq(left, right):
    if left == right:
        return [[0, 1], [arr[left], 1]]
    mid = (left + right) // 2
    arr_left = dnq(left, mid)
    arr_right = dnq(mid+1, right)
    temp_arr = []
    for sum_l, cnt_l in arr_left:
        for sum_r, cnt_r in arr_right:
            new_sum = sum_l + sum_r
            if new_sum > C:
                continue
            new_cnt = cnt_l * cnt_r

            for elem in temp_arr:
                if elem[0] == new_sum:
                    elem[1] += new_cnt
                    break
            else:
                temp_arr.append([new_sum, new_cnt])
    return temp_arr

ans_arr = dnq(0, N-1)
ans = 0
for elem in ans_arr:
    ans += elem[1]
print(ans)