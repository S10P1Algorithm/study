s1 = input()
s2 = input()
vec = [' '] * 1000000

levelS1 = len(s1)
levelS2 = len(s2) - 1
idx = 0
idxW1 = 0

while idx < levelS1:
    vec[idx] = s1[idxW1]
    idx += 1
    idxW1 += 1
    idxW2 = levelS2

    while idxW2 >= 0 and idx - 1 >= idxW2 and vec[idx - 1] == s2[idxW2]:
        idx -= 1
        idxW2 -= 1

    if idxW2 != -1:
        idx += levelS2 - idxW2
    else:
        levelS1 -= (levelS2 + 1)

if levelS1 == 0:
    print("FRULA")
else:
    for i in range(levelS1):
        print(vec[i], end='')
