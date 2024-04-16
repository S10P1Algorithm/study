# def f(l, r):  # (l, r]
#     return pSum[r] - pSum[l - 1]
#
# def Sol():
#     for i in range(k, 1132501):  # sz의 값 사용
#         if i > 1132500:  # sz의 값 사용
#             return i
#         flag = True
#         for j in range(151):
#             if i in DP[j]:
#                 flag = False
#                 break
#         if flag:
#             return i
#
# n = int(input())
# v = list(map(int, input().split()))
# pSum = [0] + [sum(v[:i+1]) for i in range(n)]
# k = int(input())
#
# DP = [set() for _ in range(151)]
# t = [set() for _ in range(151)]
#
# DP[0].add(0)
# for cur in range(1, n + 1):
#     for i in range(cur):
#         t[i + 1] |= {j + f(cur - i, cur) for j in DP[i]}
#         t[0] |= DP[i]
#     for i in range(cur + 1):
#         DP[i] = t[i]
#         t[i] = set()
#
# print(Sol())
#
#

def solve():
    if k > score[1][n]:
        print(k)
        return

    DT[0][0] = True
    for i in range(1, n + 1):
        for j in range(1, i + 2):
            if j <= 2:
                DT[i][score[j][i]] = True
            else:
                DT[i] |= DT[j - 2] << score[j][i]

    ans = k
    while DT[n][ans]:
        ans += 1
    print(ans)

def main():
    input_data()
    solve()

def input_data():
    global n, k, arr, sum, score, DT
    n = int(input())
    arr = list(map(int, input().split()))
    sum = [0] * (n + 1)
    score = [[0] * n for _ in range(n)]
    DT = [0] * n
    for i in range(n):
        DT[i] = [False] * 1140000

    for i in range(1, n + 1):
        sum[i] = sum[i - 1] + arr[i]
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            score[i][j] = score[i][j - 1] + sum[j] - sum[i - 1]
    k = int(input())

if __name__ == "__main__":
    main()
