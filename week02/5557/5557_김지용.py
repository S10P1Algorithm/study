#백트래킹

N = int(input())
D = tuple(map(int, input().split()))
cnt = 0

def backtrack(n, curr):
    global cnt
    if n == N-1:
        if curr == D[N-1]:
            cnt += 1
        return
    elif n < N-1:
        curr += D[n]
        if 0 <= curr <= 20:
            backtrack(n+1, curr)
        curr -= 2*D[n]
        if 0 <= curr <= 20:
            backtrack(n+1, curr)
        curr += D[n]


backtrack(0,0)

print(cnt)