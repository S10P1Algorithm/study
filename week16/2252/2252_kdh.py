import sys
sys.stdin = open("input.txt", "r")
N, M = map(int, sys.stdin.readline().split())

adj_list = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    adj_list[A - 1].append(B - 1)

for neighbor in adj_list:
    neighbor.sort()

is_visited = [False] * N
back_num = [0] * N

idx = 0
stack = []
for i in range(N):
    if not is_visited[i]:
        is_visited[i] = True
        idx+=1
        stack.append(i)
        while stack:
            start = stack[-1]
            for j in adj_list[start]:
                if not is_visited[j]:
                    is_visited[j] = True
                    idx+=1
                    stack.append(j)
                    break
            else:
                idx+=1
                back_num[start] = idx
                stack.pop()
ans = sorted((i + 1 for i in range(N)), key=lambda x: -back_num[x-1])
print(*ans)