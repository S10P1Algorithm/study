from itertools import product

current_chanel = 100
btns = list(range(0, 10))

N = int(input())
N_len = len(str(N))
M = int(input())
M_len = len(str(M))

if current_chanel == N:
    print(0)
elif M == 10:
    print(abs(N - current_chanel))
else:
    if M != 0:
        broken_btns = list(map(int, input().split()))
        btns = list(set(btns) - set(broken_btns))

    absolute = abs(N - current_chanel)
    k = absolute

    numnum = 100

    if N_len > absolute:
        print(absolute)
    else:
        # 모든 버튼 경우 구하기
        for cwr in product(btns, repeat=N_len):
            ex_num = int(''.join(map(str, cwr)))
            target = abs(N - ex_num)
            if target < absolute:
                absolute = target
                numnum = ex_num

        # 버튼 자릿수 -1
        if N_len > 1:
            for cwr in product(btns, repeat=N_len-1):
                ex_num = int(''.join(map(str, cwr)))
                target = abs(N - ex_num)
                if target <= absolute:
                    absolute = target
                    numnum = ex_num

        # 버튼 자릿수 +1
        for cwr in product(btns, repeat=N_len+1):
            ex_num = int(''.join(map(str, cwr)))
            target = abs(N - ex_num)
            if target < absolute:
                absolute = target
                numnum = ex_num

        if k < (len(str(numnum)) + abs(N - numnum)):
            print(k)
        else:
            if numnum != 100:
                print(len(str(numnum)) + abs(N - numnum))
            elif numnum == 100 or M == 10:
                print(abs(N - numnum))
