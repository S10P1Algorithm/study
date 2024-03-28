N = int(input())
# 구매할 라면 갯수
arr = list(map(int, input().split()))
# i번 공장에서 정확하게 Ai개의 라면을 구매하기

# 1. i번 공장에서 라면 하나를 구매 = 3
# 2. i번 공장과 i+1번 공장에서 라면을 하나씩 구매 (1<=i<=N-1) = 5
# 3. i번 공장과 i+1, i+2 공장에서 라면을 하나씩 구매 = 7
# 최소의 비용으로 라면을 구매, 필요한 금액을 출력

cost = 0

for i in range(N):
    if arr[i] == 0:
        continue
    elif i+1 < N and i+2 < N:
        while arr[i] != 0 and arr[i+1] != 0 and arr[i+2] != 0:
            arr[i] -= 1
            arr[i+1] -= 1
            arr[i+2] -= 1
            cost += 7
        if arr[i] == 0:
            continue
        else:
            cost += arr[i] * 3
            arr[i] = 0
    elif i+1 < N:
        while arr[i] != 0 and arr[i+1] != 0:
            arr[i] -= 1
            arr[i+1] -= 1
            cost += 5
        if arr[i] == 0:
            continue
        else:
            cost += arr[i] * 3
            arr[i] = 0
    else:
        cost += arr[i] * 3
        arr[i] = 0

print(cost)