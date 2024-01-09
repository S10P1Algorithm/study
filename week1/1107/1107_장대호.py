channel_number = int(input())
number_of_malfnc = int(input())
zero_to_nine_number = {str(i) for i in range(10)}

# 모두 사용가능하면 0~9의 번호 사용
if number_of_malfnc == 0:
    available_num = zero_to_nine_number
# 고장난 버튼이 있으면 오작동 번호를 제거
else:
    # 사용할 수 없는 번호를 집합 연산으로 빼기 위해 set으로 받아옴
    available_num = zero_to_nine_number - set(input().split())

# 현재 번호와 이동하려는 채널 번호사이의 거리
ans = abs(channel_number - 100)
# 500000 < 으로 가기 위해 0에서 오름차순 접근
# 또는, 999999에서 내림차순으로 접근
for n in range(1000000):
    # num에 사용가능한 번호가 포함되어있는지 확인하기 위해 str 변환
    num = str(n)
    for i in range(len(num)):
    # 사용가능한 숫자가 아니라면
        if num[i] not in available_num:
            break #해당 숫자는 폐기
        # 다 돌았다면, 차이만큼 +, - 버튼 횟수화, 숫자 입력을 위한 버튼 횟수를 더한 값의 최솟값을 갱신
        if i == len(num)-1:
            ans = min(ans, abs(channel_number - n) + len(num))

print(ans)