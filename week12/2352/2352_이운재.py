import sys

input = sys.stdin.readline

def bi(start,end, target):
    global lst
    while start < end:
        mid = (start+end) // 2

        if lst[mid] < target:
            start = mid + 1
        else:
            end = mid
    return end

N = int(input())

arr = list(map(int,input().split()))
lst = []

for i in range(N):
    if i == 0:
        lst.append(arr[i])
    else:
        if arr[i] > lst[-1]:
            lst.append(arr[i])
        else:
            lst[bi(0, len(lst), arr[i])] = arr[i]

print(len(lst))