# n = int(input())
# arr = list(map(int,input().split()))
# cnt = 0
# for i in range(n):
#     base = arr[i]
#     temp = 0 
#     for j in range(i+1,n):
#         if arr[j] > base :
#             temp += 1
#     if temp > cnt :
#         cnt = temp
# print(cnt)

# x = int(input())

# arr = list(map(int, input().split()))

# dp = [1 for i in range(x)]

# for i in range(x):
#     for j in range(i):
#         if arr[i] > arr[j]:
#             dp[i] = max(dp[i], dp[j]+1)

# print(max(dp))
N = int(input())  
arr = list(map(int, input().split()))  

## 이진탐색 함수
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

lis = [arr[0]]

for i in range(1, len(arr)):
    if arr[i] > lis[-1]:
        lis.append(arr[i])
    else:
        index = binary_search(lis, arr[i])
        lis[index] = arr[i]
    print(lis)
print(len(lis))