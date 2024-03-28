import sys

input = sys.stdin.readline

N,M = map(int,input().split())

mx_tr = [0] * (N*2)
mn_tr = [0] * (N*2)

def make_mx_tr(N):
    for i in range(N-1,0,-1):
        mx_tr[i] = max(mx_tr[2*i], mx_tr[2*i+1])

def make_mn_tr(N):
    for i in range(N-1,0,-1):
        mn_tr[i] = min(mn_tr[2*i], mn_tr[2*i+1])

def find_max_min(start,end):
    start += N
    end += N
    max_v = 0
    min_v = 1000000000
    while start <= end:
        if start % 2 == 1:
            max_v = max(max_v, mx_tr[start])
            min_v = min(min_v, mn_tr[start])
            start += 1
        if end % 2 == 0:
            max_v = max(max_v, mx_tr[end])
            min_v = min(min_v, mn_tr[end])
            end -= 1
        start //= 2
        end //= 2
    return (max_v, min_v)


for i in range(N):
    x = int(input())
    mx_tr[N+i] = x
    mn_tr[N+i] = x
make_mn_tr(N)
make_mx_tr(N)

for i in range(M):
    start, end = map(int,input().split())
    # x = find_min(start-1, end-1)
    x = find_max_min(start-1, end-1)
    print(x[1],x[0])