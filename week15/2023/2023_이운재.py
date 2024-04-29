import sys
input = sys.stdin.readline

def is_prime(num):
    if num % 2 == 0:
        return False
    for i in range(3, int(num/2)+1):
        if num % i == 0:
            return False
    return True

def dfs(num):
    if len(str(num)) == n:
        print(num)
        return
    else:
        for i in range(1, 10):
            if is_prime(num*10+i):
                dfs(num*10+i)

n = int(input())

dfs(2)
dfs(3)
dfs(5)
dfs(7)