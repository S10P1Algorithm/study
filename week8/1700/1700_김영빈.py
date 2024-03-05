n, k = map(int, input().split())
num = list(map(int, input().split()))

lst = []
cnt = 0
for i in range(k):
    if num[i] in lst:
        continue
    if len(lst) < n:
        lst.append(num[i])
        continue
    temp = 0
    last = 0
    for li in lst:
        if li not in num[i:]:
            temp = li
            break
        elif num[i:].index(li) > last:
            last = num[i:].index(li)
            temp = li
    lst[lst.index(temp)] = num[i]
    cnt += 1
print(cnt)
