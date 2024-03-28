def slump(str_input):
    idx = 0

    if str_input == '':
        return False

    if str_input[idx] != 'D' and str_input[idx] != 'E':
        return False

    if str_input[-1] != 'G':
        return False

    idx += 1

    if str_input[idx] != 'F':
        return False

    while str_input[idx] == 'F':
        idx += 1

    if str_input[idx] == 'G' or slump(str_input[idx:]):
        return True

    return False


def slimp(str_input):
    idx = 0

    if str_input == '':
        return False

    if str_input[idx] != 'A':
        return False
    idx += 1

    l = len(str_input)

    if l == 1:
        return True

    if l == 2 and str_input[idx] == 'H':
        return True

    if l > 2:
        if str_input[-1] != 'C':
            return False
        if str_input[idx] == 'B' and slimp(str_input[idx+1:-1]):
            return True
        if slump(str_input[idx:-1]):
            return True
        return False


def findDE(str_input):
    result = []
    l = len(str_input)
    for i in range(l):
        if str_input[i] == 'D' or str_input[i] == 'E':
            result.append(i)
    return result


N = int(input())

print('SLURPYS OUTPUT')

for _ in range(N):
    curr = input()
    idxs = findDE(curr)

    isSlurpy = "NO"

    for idx in idxs:

        if slimp(curr[:idx]) and slump(curr[idx:]):

            isSlurpy = 'YES'

    print(isSlurpy)

print('END OF OUTPUT')
