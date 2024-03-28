goal_num = int(input())
number_of_broken_num = int(input())
if number_of_broken_num != 0:

    broken_num = list(map(int,input().split()))
else :
    broken_num = []
# print(goal_num,number_of_broken_num,broken_num)
minus_goal_num = goal_num
plus_goal_num = goal_num


res_minus = 0
res_plus = 0
if goal_num == 100 : 
    print(0)
elif number_of_broken_num == 0:
    print(min(abs(goal_num-100),len(str(goal_num))))
elif number_of_broken_num == 10:
    print(abs(goal_num-100))
else :
    while 1:
        
        minus_goal_num -=1
        res_minus+=1
        for i in str(minus_goal_num):
            if  minus_goal_num<0:
                break
            elif int(i) in broken_num:
                break
        else :
            res_minus = min(res_minus+len(str(minus_goal_num)),len(str(goal_num)))
            print(res_minus)
            break

        plus_goal_num +=1
        res_plus+=1
        for j in str(plus_goal_num):
            if int(j) in broken_num:
                break
        else :
            res_plus =min(res_plus+len(str(plus_goal_num)),len(str(goal_num)))
            print(res_plus)
            break



