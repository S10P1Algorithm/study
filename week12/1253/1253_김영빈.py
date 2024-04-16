n = int(input())
arr = list(map(int,input().split()))
arr.sort()

cnt = 0
for i in range(n):
    start = 0 
    end = n - 1
    goal = arr[i]
    while start < end:
        if arr[start] + arr[end] == goal :
            if start == i :
                start += 1
            elif end == i :
                end -= 1
            else : 
                cnt +=1
                break
        elif arr[start] + arr[end] < goal :
            start += 1
        else :
            end -= 1
print(cnt)