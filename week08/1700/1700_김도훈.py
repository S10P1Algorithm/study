N, K = map(int, input().split())
order = list(map(int, input().split()))
plug = [0] * N

ans = 0
for i in range(K):
    check = False
    for j in range(N):
        if order[i] == plug[j]:
            check = True
            break
    if check:
        continue

    for j in range(N):
        if plug[j] == 0:
            plug[j] = order[i]
            check = True
            break
    if check:
        continue

    last_used_idx = -1
    last_used_div = -1
    for j in range(N):
        temp = 0
        for k in range(i + 1, K):
            if plug[j] == order[k]:
                break
            temp += 1
        if temp > last_used_idx:
            last_used_idx = temp
            last_used_div = j
    plug[last_used_div] = order[i]
    ans += 1

print(ans)
