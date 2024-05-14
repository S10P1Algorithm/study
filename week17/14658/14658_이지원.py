import sys

N, M, L, K = map(int, sys.stdin.readline().split())
arr = [None for _ in range(K)]

for i in range(K):
    arr[i] = tuple(map(int, sys.stdin.readline().split()))

ans = K

for i, _ in arr:
    for _, j in arr:
        temp = K
        for k, l in arr:
            if i <= k <= i + L and j <= l <= j + L:
                temp -= 1

        ans = min(ans, temp)

print(ans)