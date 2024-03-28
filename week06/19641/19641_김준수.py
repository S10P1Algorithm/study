import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N):
    input_list = list(map(int, input().split()))
    node = input_list[0]
    for i in sorted(input_list[1:-1]):
        graph[node].append(i)

root = int(input())
tree = [[0, 0] for _ in range(N+1)]


def dfs(cur, order):
    tree[cur][0] = order
    for next in graph[cur]:
        if tree[next][0]:
            continue
        order = dfs(next, order+1)
    tree[cur][1] = order + 1
    return order + 1


dfs(root, 1)
for i in range(1, N+1):
    print(i, tree[i][0], tree[i][1])
