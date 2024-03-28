import sys
sys.stdin = open('input.txt', 'r')
import math
N = int(input())
A_arr = list(map(int, input().split()))
B_arr = list(map(int, input().split()))

gifticon = list(map(lambda x, y: [x, y], A_arr, B_arr))
gifticon.sort(key=lambda x: (x[1], x[0]))

ans = 0
prev_max_exp = 0
max_exp = 0
max_dest = 0
for exp, dest in gifticon:

    if exp < dest:
        add2 = math.ceil((dest-exp)/30)
        exp += add2 * 30
        ans += add2
        

    if max_dest < dest:
        max_dest = dest
        prev_max_exp = max_exp

    if exp < prev_max_exp:
        add1 = math.ceil((prev_max_exp-exp)/30)
        exp += add1 * 30
        ans += add1  

    max_exp = max(max_exp, exp)
print(ans)