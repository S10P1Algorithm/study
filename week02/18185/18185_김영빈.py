N=int(input())
A = list(map(int, input().split())) + [0,0]
result = 0 # 합계 가격
length = len(A)
for i in range(len(A)-2):
    # 2번째가 더 크면 3개 사면 손해임
    # 1 2 1 1
    if A[i+1] > A[i+2]:
        Min = min(A[i],A[i+1]-A[i+2])
        A[i]-=Min
        A[i+1]-=Min
        result += Min*5
        # 3개 연속 구매
        Min_3 = min(A[i:i+3])
        A[i]-=Min_3
        A[i+1]-=Min_3
        A[i+2]-=Min_3
        result += Min_3*7
        # 1개 구매
        result += A[i]*3

    else :
        # 3개 구매
        Min_3 = min(A[i:i+3])
        A[i]-=Min_3
        A[i+1]-=Min_3
        A[i+2]-=Min_3
        result += Min_3*7

        # 2개 구매
        Min_2 = min(A[i:i+2])
        A[i]-=Min_2
        A[i+1]-=Min_2
        result+=Min_2*5

        # 1개 구매
        result += A[i]*3


    
    

print(result)
        