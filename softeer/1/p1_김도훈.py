import sys
sys.stdin = open('input.txt', 'r')
N = int(input())
cctv = list(input())

# p는 사람수
is_valid = True
P = 0
U = 0
for chr in cctv:
    if chr == '(':
        P += 1
    elif chr == ')':
        P -= 1
    else:
        U += 1
# U가 전체 ? 갯수, x가 그중 ( 갯수 ) 는 U-x => (U-x) - x = P 가 되도록
# x = (U-P) // 2     
unknown = []
if U:
    if (U-P) % 2:
        is_valid = False
    else:
        x = (U-P)//2
        if x < 0:
            is_valid = False
        else:
            for i in range(x):
                unknown.append('(')
            for i in range(U-x):
                unknown.append(')')        
else:
    if P:
        is_valid = False

# ? 를 모두 ((( ... ))) 로 치환한후 validation check
# ( 갯수만큼 앞에 몰아넣고 ) 는 뒤에 몰아넣는다
if unknown:
    valid = 0
    index = 0
    for char in cctv:
        if char == '(':
            valid += 1
        elif char == ')':
            valid -= 1
        else:
            if unknown[index] == '(':
                valid+=1
            else:
                valid -= 1

        if valid < 0:
            is_valid = False
            break
    if valid != 0:
        is_valid = False

if is_valid:
    print('Yes')
else:
    print('No')
print(unknown, P, U)