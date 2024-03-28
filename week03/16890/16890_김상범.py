s = input()
N = len(s)

apple = list(s)

s = input()
cube = list(s)

apple.sort()
cube.sort()

xleft, xRight = 0, N // 2 + N % 2 - 1
yleft, yRight = N - 1 - N // 2 + 1, N - 1

leftend, rightend = 0, N - 1
ans = [''] * N

for i in range(N):
    if i % 2:
        if cube[yRight] <= apple[xleft] and i != N - 1:
            ans[rightend] = cube[yleft]
            rightend -= 1
            yleft += 1
        else:
            ans[leftend] = cube[yRight]
            leftend += 1
            yRight -= 1
    else:
        if apple[xleft] >= cube[yRight] and i != N - 1:
            ans[rightend] = apple[xRight]
            rightend -= 1
            xRight -= 1
        else:
            ans[leftend] = apple[xleft]
            leftend += 1
            xleft += 1

result = ''.join(ans)
print(result)
