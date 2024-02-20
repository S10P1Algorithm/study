print("SLURPYS OUTPUT")
N = int(input())

for _ in range(N):
    stack = []
    s = input().strip()
    SWITCH = True

    if s[0] != 'A' or s[-1] != 'G':
        print("NO")
        continue

    for c in s:
        if c == 'A':
            if stack and stack[-1] == 2:
                SWITCH = False
                break
            stack.append(1)
        elif c == 'B':
            if not stack or stack[-1] == 2:
                SWITCH = False
                break
        elif c == 'C':
            if stack:
                while stack[-1] == 2:
                    stack.pop()
                if not stack:
                    SWITCH = False
                    break
                stack.pop()
            else:
                SWITCH = False
                break
        elif c in ['D', 'E']:
            stack.append(2)
        elif c == 'F':
            if not stack or stack[-1] == 1:
                SWITCH = False
                break
        elif c == 'H':
            if s.index(c) != 0 and s[s.index(c) - 1] == 'A':
                stack.pop()
            else:
                SWITCH = False
                break
        elif c == 'G':
            if not stack or stack[-1] == 1 or (s.index(c) and s[s.index(c) - 1] not in ['G', 'F']):
                SWITCH = False
                break
            else:
                while stack[-1] == 2:
                    stack.pop()
        else:
            SWITCH = False
            break

    if SWITCH and not stack:
        print("YES")
    else:
        print("NO")

print("END OF OUTPUT")
