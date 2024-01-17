# 벨만 포드 같은데 문제가 ...

import sys

input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())

edges = []

earn_gold = [INF] * (v+1)

for _ in range(e):
    now, next, gold = map(int,input().split())

    edges.append((now,next,-gold))

def bellman_ford(start):

    earn_gold[start] = 0

    for i in range(v):
        for j in range(e):
            now_node = edges[j][0]
            next_node = edges[j][1]
            gold_amount = edges[j][2]

            if earn_gold[now_node] != INF and earn_gold[next_node] > earn_gold[now_node] + gold_amount:
                earn_gold[next_node] = earn_gold[now_node] + gold_amount
                if i == v-1:
                    return True
    
    return False

loop = bellman_ford(1)


dic = dict()

if loop:
    print('-1')
    flag = False
else:
    for i in range(2,v+1):
        dic[i] = earn_gold[i]
    
    order = sorted(dic.items(), key=lambda x: -x[1])

    answer = [1,]

    for i in order:
        answer.append(i[0])
    
    print(*answer)



