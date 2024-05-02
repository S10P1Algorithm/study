## 에라토스테네스의 체 : 메모리 초과
# N = int(input())

# result = [2, 3, 5, 7]

# if N == 1:
#     print(*result, sep='\n')

# end = 10 ** N

# prime = [True for i in range(end)]

# for i in range(2, end):
#     if prime[i]:
#         j = 2
#         while j * i < end:
#             prime[j * i] = False
#             j += 1

# k = 2

# while k <= N:
#     new = []
#     for prev in result:
#         for last in range(1, 10, 2):
#             if prime[prev * 10 + last]:
#                 new.append(prev * 10 + last)
    
#     result = new
#     k += 1

# print(*result , sep='\n')

import math

N = int(input())

def validate(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
        
    return True

result = [2, 3, 5, 7]

k = 2

while k <= N:
    new = []
    for prev in result:
        for last in range(1, 10, 2):
            if validate(prev * 10 + last):
                new.append(prev * 10 + last)
    
    result = new
    k += 1

print(*result, sep='\n')