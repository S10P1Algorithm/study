MODULO = 1000000000
lisT = [[[0 for _ in range(10)] for _ in range(1024)] for _ in range(102)]

N = int(input())

for i in range(1, 10):
    tmp = 1 << i
    lisT[1][tmp][i] = 1

for x in range(1, N+1):
    for i in range(1024):
        for j in range(10):
            if j - 1 >= 0:
                lisT[x + 1][i | 1 << (j - 1)][j - 1] += lisT[x][i][j]
                lisT[x + 1][i | 1 << (j - 1)][j - 1] %= MODULO
            if j + 1 < 10:
                lisT[x + 1][i | 1 << (j + 1)][j + 1] += lisT[x][i][j]
                lisT[x + 1][i | 1 << (j + 1)][j + 1] %= MODULO

ans = 0
for i in range(10):
    ans += lisT[N][1023][i]
    ans %= MODULO

print(ans)
