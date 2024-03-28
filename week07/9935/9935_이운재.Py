import sys
from collections import deque

input = sys.stdin.readline
s = list(input().strip())
a = input().strip()

lena = len(a)
stack = []

q = deque(s)
for i in range(len(s)):

    stack.append(q.popleft())
    if ''.join(stack[-lena:]) == a:
        for j in range(lena):
            stack.pop()

print(''.join(stack) if len(stack) > 0 else 'FRULA')
