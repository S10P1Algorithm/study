TC = int(input())
for _ in range(TC):
    N, M = map(int, input().split())

    books = [False] * (N+1)

    requests = []
    for _ in range(M):
        requests.append(list(map(int, input().split())))
    requests.sort(key=lambda x: x[1])

    cnt = 0
    while requests:
        a, b = requests.pop(0)

        for i in range(a, b+1):
            if not books[i]:
                cnt += 1
                books[i] = True
                break

    print(cnt)