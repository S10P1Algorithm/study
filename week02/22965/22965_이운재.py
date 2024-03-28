'''
K조각을 자를수 있는 칼이 있다 => 그 칼로 매 턴 마다 무한 썰기 가능.
최대, 최소, neither 가 최대 값이다. 그래서 나올 수 있는 경우의 수는 3

'''

n = int(input())
arr = [0]+ list(map(int, input().split()))

ans = 1
cnt = 0
m = 1e9
arr[0] = -1e9
sorted_arr = True
flag = True

for i in range(1, n +1):
    if arr[i] < arr[i - 1]:
        sorted_arr = False
        cnt += 1
    if cnt and arr[i] > arr[1]:
        flag = False

if sorted_arr:
    print("1")
elif cnt == 1 and flag:
    print("2")
else:
    print("3")









'''
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



