import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
numbers = list(map(int, input().split()))

ans = list([0]*21 for _ in range(N-1))
ans[0][numbers[0]] += 1

for i in range(1, N-1):
    for j in range(21):
        cnt = ans[i-1][j]
        if cnt:
            if 0 <= j+numbers[i] <= 20:
                ans[i][j+numbers[i]] += cnt
            if 0 <= j-numbers[i] <= 20:
                ans[i][j-numbers[i]] += cnt

print(ans[N-2][numbers[N-1]])

