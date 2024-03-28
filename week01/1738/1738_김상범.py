N, M = map(int,input().split())

adj_lst = [[float('inf')] * N for _ in range(N)]

for _ in range(M):
    u, v, w = map(int, input().split())
    adj_lst[u - 1][v - 1] = - w
    
# print(*adj_lst, sep='\n')
# print()
power = [float('inf')] * N
road = [0 for _ in range(N + 1)]
power[0] = 0
# print(porow)
cycle = {} 
def bella():
    for case in range(N):
        is_change = False
        for start in range(N):
            for end in range(N):
                if adj_lst[start][end] + power[start] < power[end]:
                    power[end] = adj_lst[start][end] + power[start]
                    road[end + 1] = start + 1
                    is_change = True
                    if case == N - 1:
                        power[end] = -float('inf')
        if not is_change:
            return True

    
alert = []
bella()
# print(power)
# print(road)
if power[N - 1] != -float('inf'):
    tmp = []
    start = N
    while start != 0:
        tmp.append(start)
        start = road[start]
        # print(start)
    print(' '.join(map(str, tmp[::-1])))
else:
    print(-1)
