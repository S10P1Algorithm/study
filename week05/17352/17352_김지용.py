import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    return find(parent[x])


def join(x, y):
    x_root, y_root = find(x), find(y)

    if y_root < x_root:
        parent[x_root] = y_root
        parent[x] = y_root
    else:
        parent[y_root] = x_root
        parent[y] = x_root


N = int(input())

parent = [i for i in range(N + 1)]

for _ in range(N - 2):
    a, b = map(int, input().split())
    join(a, b)

for i in range(1, N+1):
    parent[i] = find(i)

curr = parent[1]
result = 0

for i in range(2, N + 1):
    if parent[i] != curr:
        result = i
        break

print(1, result)
