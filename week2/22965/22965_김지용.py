N = int(input())

A = tuple(map(int, input().split()))
cnt = 1

i = 0

# 순차적으로 보면서 값이 떨어 지는 부분을 찾아 잘라서 재배열
while i < N-1:
    curr = A[i]
    next_node = A[i+1]
    if curr > next_node:
        cnt += 1
    i += 1

print(cnt)