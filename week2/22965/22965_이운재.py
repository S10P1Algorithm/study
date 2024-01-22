def partition(a,begin,end):
    global res
    pivot = (begin + end) // 2
    L = begin
    R = end
    while L <= R:
        while L <= R and a[L] < a[pivot]:
            L += 1
        while L <= R and a[R] >= a[pivot]:
            R -= 1
        if L < R:
            if L == pivot: pivot = R
            a[L], a[R] = a[R], a[L]
            res += 1
    a[pivot], a[R] = a[R], a[pivot]
    

N = int(input())
arr = list(map(int, input().split()))

res = 0        
partition(arr,0,N-1)
print(res+1)     
'''

arr2 = sorted(arr)

ans = arr[0]-arr2[0]

res = 1
for i in range(1,N):

    if ans != arr[i] - arr2[i]:
        res += 1
        ans = arr[i] - arr2[i]

print(res)
틀렸다.

'''
'''
tmp = 0

res = 0

for i in range(1, N):
    if arr[i] < arr[i-1]:
        tmp += 1
    else:
        tmp = 0
    
    res = max(res, tmp)

print(res+1)
이거 또한 틀렸다.
'''



