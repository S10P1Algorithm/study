N = int(input())
M = int(input())

num_list = list(range(0, 10))
if M:
    arr = list(map(int, input().split()))
    for i in arr:
        num_list.remove(i)

ans = abs(100 - N)
N_digit = 0
temp = N

if N:
    while temp:
        temp //=10
        N_digit+=1
else:
    N_digit = 1

def backtrack(num, digit):
    global ans
    if digit == 0:
        ans = min(ans, abs(num-N) + N_digit)
    else:
        for i in num_list:
            new_num = num + i * 10**(digit-1)
            backtrack(new_num, digit-1)

if M == 10:
    print(ans)
elif M == 0:
    ans = min(ans, N_digit)
    print(ans)
else:
    N_digit+=1
    while N_digit:
        backtrack(0, N_digit)
        N_digit-=1
    print(ans)