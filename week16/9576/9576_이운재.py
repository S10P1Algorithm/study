import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    book, student = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(student)]
    arr.sort(key=lambda x: x[1])

    res = [0] * (book + 1)

    for i in range(student):
        for j in range(arr[i][0], arr[i][1] + 1):
            if res[j] == 0:
                res[j] = 1
                break
    print(sum(res))

