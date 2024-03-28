N = int(input())
A = list(map(int, input().split()))

len_A = len(A)

# 
cnt = 1
result = []
res_cnt = 0

while len(result) != len_A :
    for i in range(len(A)):
        
        if A[i] == cnt :
            j=i
            while A[j] == cnt:
                
                result.append(A[j])
                cnt+=1
                j+=1
                # print(j)
                if j == len(A) :
                    break
                # print(j,cnt,'cnt')
    # 차집합
    A = list(filter(lambda x: x not in result, A))
    res_cnt += 1
    # print('0000000000000000000000000')
# print(result)
print(res_cnt)