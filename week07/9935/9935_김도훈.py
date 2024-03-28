import sys
sys.stdin = open('input.txt', 'r')

ans = input()
bomb = input()
stack = [''] * len(ans)

for i in range(len(ans)):
    stack.append(ans[i])

    if len(stack) >= len(bomb):
        check_bomb = True
        for j in range(len(bomb)):
            if stack[-1-j] != bomb[len(bomb)-j-1]:
                check_bomb = False
                break
        if check_bomb:
            for _ in range(len(bomb)):
                stack.pop() # del 하면 더 빠를듯


ans = ''.join(stack)
if ans:
    print(ans)
else:
    print('FRULA')