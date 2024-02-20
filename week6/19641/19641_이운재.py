import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(root, turn):
    tree[root][0] = turn
    for next in graph[root]:
        if tree[next][0]:
            continue
        turn = dfs(next,turn + 1)
    tree[root][1] = turn + 1
    return turn + 1


N = int(input())

graph = [[] for _ in range(N+1)]

for i in range(N):
    input_value = list(map(int,input().split()))
    node = input_value[0]
    input_value = sorted(input_value[1:-1])

    for i in input_value:
        graph[node].append(i)

tree = [[0,0] for _ in range(N+1)]

root = int(input())
dfs(root,1)

for i in range(1,N+1):
    print(i, tree[i][0], tree[i][1])




