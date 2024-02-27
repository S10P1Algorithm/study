import sys
arr=sys.stdin.readline().rstrip()
str=sys.stdin.readline().rstrip()
stack=[]
for i in arr:
    stack.append(i)
    
    if ''.join(stack[-len(str):])==str:
        for _ in range(len(str)):
            stack.pop()
            

if len(stack)>0:
    print(*stack,sep='')
else:
    print('FRULA')