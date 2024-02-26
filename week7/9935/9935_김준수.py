import sys
input = sys.stdin.readline

target = list(input().rstrip())
bomb = list(input().rstrip())

b_length = len(bomb)
stack = []

for s in target:
    stack.append(s)
    if stack[len(stack)-b_length:len(stack)] == bomb:
        for _ in range(b_length):
            stack.pop()
else:
    if stack:
        print(''.join(stack))
    else:
        print('FRULA')
