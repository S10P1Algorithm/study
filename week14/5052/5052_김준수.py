import sys
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(0, T):
    N = int(input().rstrip())

    numbers = []
    for _ in range(0, N):
        numbers.append(input().rstrip())

    numbers.sort()

    answer = True
    for i in range(0, N-1):
        if numbers[i] == numbers[i+1][:len(numbers[i])]:
            answer = False
            break

    if answer:
        print("YES")
    else:
        print("NO")
