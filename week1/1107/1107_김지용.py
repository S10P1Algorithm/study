# 숫자로 입력 해서 갈 수 있는 채널 인지 확인
def check_number(num1, err_btn):
    result = True
    for i in list(str(num1)):
        if int(i) in err_btn:
            result = False
    return result


# 숫자로 입력할 수 있는 가장 가까운 채널 찾기
# 아예 없을 경우 100으로 설정
def find_closest(N, err_btn):
    for i in range(500000):
        if N-i >= 0 and check_number(N-i, err_btn):
            return N - i
        if check_number(N+i, err_btn):
            return N + i
    return 100


N = int(input())
M = int(input())

error_btn = ()

if M:
    error_btn = tuple(map(int, input().split()))

# 고장난 버튼이 없을 경우 바로 도달 가능
if error_btn:
    closest = find_closest(N, error_btn)
else:
    closest = N

# 100에서 바로 가는 경우랑 갈 수 있는 가까운 숫자에서 가는 경우 중 더 가까운 경우를 출력
print(min(abs(100-N), len(list(str(closest)))+abs(N-closest)))