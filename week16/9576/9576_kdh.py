import sys
sys.stdin = open("input.txt", "r")

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N, M = map(int, input().strip().split())
    book_list = []
    for _ in range(M):
        book_range = list(map(int, input().split()))
        book_list.append(book_range)
    
    book_list = sorted(book_list, key=lambda x: (x[1], x[0]))
    book_used = [False] * (N + 1)
    ans = 0
    for book in book_list:
        for book_num in range(book[0], book[1] + 1):
            if not book_used[book_num]:
                book_used[book_num] = True
                ans += 1
                break
    print(ans)