T = int(input())


test1 = dict()

for tc in range(1,T+1):
    N = int(input())
    encryted = []

    for i in range(N):
        encryted.append(input())

    decoded = input()
    problem = input()

    # 1.무지성 딕셔너리 생성

    for i in range(N):
        if len(decoded) != len(encryted[i]):
            continue
        else:
            for j in range(len(encryted[i])):
                if encryted[i][j] in test1.keys() and decoded[j] != test1[encryted[i][j]]:
                    del test1[encryted[i][j]]
                else:
                    test1[encryted[i][j]] = decoded[j]

    res = ''

    for i in problem:
        try:
            res += test1[i]
        except:
            res += '?'

    print(res)
