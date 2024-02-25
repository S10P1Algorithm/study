import sys

N = int(sys.stdin.readline())

dp = {}

mod = 1000000000

def func(curr, n, visited):
    visited |= 1 << curr

    if n == N:
        if visited == 1023:
            return 1
        
        return 0
    
    res = dp.get((curr, n, visited), 0)

    if res != 0:
        return res
    
    if curr + 1 <= 9:
        res += func(curr + 1, n + 1, visited)
        
    if curr - 1 >= 0:
        res += func(curr - 1, n + 1, visited)

    res %= mod

    dp[(curr, n, visited)] = res

    return res


if N < 10:
    print(0)

elif N == 10:
    print(1)

else:
    res = 0
    for i in range(1, 10):
        v = 1 << i
        if i + 1 <= 9:
            res += func(i + 1, 2, v)

        if i - 1 >= 0:
            res += func(i - 1, 2, v)

    print(res % mod)