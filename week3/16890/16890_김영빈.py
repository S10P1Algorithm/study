import math
a = list(input())
b = list(input())
N = len(a)
sorted_a = sorted(a)[0:math.ceil(N/2)]
# sorted_b = sorted(a)[0:math.floor(N/2)]
sorted_b = sorted(list(reversed(sorted(b)))[0:math.floor(N/2)])
# sorted_b = list(reversed(sorted(b)))
# print(sorted_a)
# print(sorted_b)

result =[0]*N
left = 0
right = len(sorted_b)-1
cnt_0 = 0
while 1:
    if right == -1:
        for i in range(len(result)):
            if result[i] == 0:
                result[i]= sorted_a[left]
                cnt_0 = -1
    if cnt_0 == -1:
        break
    cnt_0 = 0
    if sorted_a[left]>=sorted_b[right]:
    #    print(sorted_a[left],sorted_b[right],'44433')
       for i in range(N-1,-1,-1):    
           if result[i] == 0:
                result[i] = sorted_a[left]
                left+=1
                break
    else:
        
        for i in range(N):
            if result[i] == 0:
                result[i]=sorted_a[left]
                left+=1
                break

    for i in result:
        if i == 0:
            cnt_0+=1
    if cnt_0 == 0:
     
        break

    cnt_0 =0 
    for i in result:
        if i == 0:
            cnt_0+=1
    if cnt_0 == 1:
        for i in range(N):
            if result[i]==0:
                result[i]=sorted_b[right]
    if cnt_0 == 1:

        break
    
    cnt_0 =0

    # print(result,'result_1')
    # print(left,right,'leftright')
    if sorted_b[right]>=sorted_a[left]:
        for i in range(N):
            if result[i]==0:
                result[i]=sorted_b[right]
                break
        right-=1
    else:
        for i in result[::-1]:    
            if i == 0:
                result[i] = sorted_b[right]
                right-=1    
                break

    for i in result:
        if i == 0:
            cnt_0+=1
    if cnt_0 == 0:
        break
    
    # print(result,'result')   
    # print(left,right,'1112')
print(''.join(result))
