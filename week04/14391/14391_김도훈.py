import sys
sys.stdin = open('input.txt', 'r')
N, M = map(int, input().split())

arr = [list(map(int, input())) for _ in range(N)]


visited = 1<<(M*N)
ans = 0
for bit in range(visited):
    local_ans = 0
    for i in range(N):
        temp = 0
        for j in range(M):
            if bit&(1<<((N-i-1) * M + M-j -1)):         
                temp *= 10
                temp += arr[i][j]
            else:
                local_ans += temp
                temp = 0
        local_ans += temp

    for j in range(M):
        temp = 0
        for i in range(N):
            if ~bit&(1<<((N-i-1) * M + M-j -1)):
                temp *= 10
                temp += arr[i][j]
            else:
                local_ans += temp
                temp = 0
        local_ans += temp

    ans = max(ans, local_ans)
print(ans)