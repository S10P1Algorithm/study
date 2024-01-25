import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
A = list(map(int, input().split()))

arr = [[0, 0, 0] for _ in range(N)]
arr[0] = [A[0]-min(A[0], A[1]), min(A[0], A[1]), 0]
arr[1] = [A[1]-min(A[0], A[1]), 0, 0]


for i in range(2, N):
    new = A[i]
    add_5 = min(new,  arr[i-1][0])
    new -= add_5
    arr[i-1][0] -= add_5
    arr[i-1][1] = add_5
    if new:
        add_7 = min(new, arr[i-2][1])
        new -= add_7
        arr[i-2][1] -= add_7
        arr[i-2][2] = add_7
    if new:
        add_3 = new
        arr[i][0] = add_3


ans = 0
for i in range(N):
    ans += arr[i][0]*3 + arr[i][1]*5 + arr[i][2]*7

print(ans)