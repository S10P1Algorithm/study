import sys
# sys.setrecursionlimit(2000)

N = int(sys.stdin.readline())

# base = set()
# child = {}
# ans = []

# for _ in range(N):
#     directory = sys.stdin.readline().rstrip().split('\\')
#     for i, d in enumerate(directory):
#         child.setdefault(f'{d}_{i}', set())
#         if i == 0:
#             base.add(d)
#         else:
#             child[f'{directory[i-1]}_{i-1}'].add(d)

# def solution(key, depth=0):
#     ans.append(' ' * depth + key)

#     for c in sorted(child[f'{key}_{depth}']):
#         solution(c, depth + 1)

# for b in sorted(base):
#     solution(b)

# print(*ans, sep='\n')

inp = set()
for _ in range(N):
    d = sys.stdin.readline().rstrip().split('\\')
    for i in range(len(d)):
        inp.add(tuple(d[0:i+1]))

    
for directory in sorted(inp):
    print(' ' * (len(directory)-1) + directory[-1])