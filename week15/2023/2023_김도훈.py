import sys

N = int(input())
dp = [[] for _ in range(N)]
dp[0].extend([2, 3, 5, 7])

def is_prime(number):
    max_verf = int(round((number)**0.5, 0))
    for i in range(2, max_verf):
        if number % i:
            continue
        else:
            return False
    return True



for i in range(N-1):
    for number in dp[i]:
        for j in [1, 3, 7, 9]:
            new_num = number*10 + j
            if is_prime(new_num):
                dp[i+1].append(new_num)

for elem in dp[N-1]:
    print(elem)