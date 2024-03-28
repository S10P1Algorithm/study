import re

slump = re.compile('([DE]F+)+G$')
slimp = re.compile('AB.+C$')
slimp2 = re.compile('A.+C$')


def isSlimp(string):
    m2 = slimp.match(string)
    m3 = slimp2.match(string)
    if m2 is not None:
        return isSlimp(string[2:len(string)-1])
    elif m3 is not None:
        m4 = slump.match(string[1:len(string)-1])
        if m4 is not None:
            return True
        else:
            return False
    elif string == 'AH':
        return True
    else:
        return False


print('SLURPYS OUTPUT')
N = int(input())
for _ in range(N):
    string = input()
    m1 = slump.search(string)
    if m1 is not None:
        if m1.span()[0] > 2:
            string2 = string[:m1.span()[0]]
            if isSlimp(string2):
                print('YES')
            else:
                print('NO')
        elif m1.span()[0] == 2:
            if string[:2] == 'AH':
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('END OF OUTPUT')
