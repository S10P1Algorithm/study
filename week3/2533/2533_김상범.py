from collections import defaultdict

parents = [0] * 1000000
visited = [0] * 1000000
map_dict = defaultdict(int)

N = int(input())
childs = []

for _ in range(N):
    a, b = map(int, input().split())
    parents[b] = a
    if a in map_dict:
        del map_dict[a]
    map_dict[b] = 1

childs = list(map_dict.keys())
ans = 0

for child in childs:
    visited[child] = 1

while childs:
    new_child = []

    for child in childs:
        if visited[child] == 1:
            if visited[parents[child]] != 2 and parents[child] != 0:
                visited[parents[child]] = 2
                new_child.append(parents[child])
                ans += 1
        else:
            if not visited[parents[child]]:
                visited[parents[child]] = 1
                if parents[child] != 0:
                    new_child.append(parents[child])

    childs = new_child

print(ans)
