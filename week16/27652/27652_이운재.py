N = int(input())

A = []
B = []
res = 0
for _ in range(N):
    a,*b = input().split()
    if a == 'add':
        if b[0] == 'A':
            A.append(b[1])
        else:
            B.append(b[1])
    elif a == 'delete':
        if b[0] == 'A':
            A.remove(b[1])
        else:
            B.remove(b[1])
    else:
        tmp = []
        for i in A:
            for j in B:
                if len(i+j) < len(b[0]):
                    continue
                else:
                    for k in range(1,len(b[0])):

                        if i[:k] + j[-(len(b[0])-k):] == b[0] and (i,j,i[:k],j[-(len(b[0])-k):]) not in tmp:
                            res +=1
                            tmp.append((i,j,i[:k],j[-(len(b[0])-k):]))
        print(res)
        res = 0

