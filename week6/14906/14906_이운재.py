N = int(input())

def slump(s):
    if len(s) <3 :
        return False
    if s[1] != 'F':
        return False
    if s[0] != 'D' and s[0] != 'E':
        return False
    else:
        for i in range(1,len(s)-1):
            if s[i] == 'F':
                continue
            else:
                a = slump(s[i:])
                if a == False:
                    return False

    if s[-1] != 'G':
        return False
    return True

def slimp(s): #ABABAHC, #ADGC
    if s[0] != 'A':
        return False
    if len(s) == 2 and s[1] == 'H':
        return True
    if len(s) > 3 and s[1] == 'B':
        if len(s) == 3:
            return False
        else:
            if not slimp(s[2:-1]):
                return False
    else:
        if not slump(s[1:-1]):
            return False

    if s[-1] != 'C':
        return False
    return True


print('SLURPYS OUT')
for i in range(N):
    s = input()
    if s[0] != 'A':
        print('NO')
    else:
        tmp = 0
        for i in range(len(s)):
            if s[i] == 'C':
                tmp = i
            elif s[i] == 'H':
                tmp = i

        a = slimp(s[:tmp+1])
        b = slump(s[tmp+1:])

        if a and b:
            print('YES')
        else:
            print('NO')
print('END OF OUTPUT')

# 8% 까지 맞음
