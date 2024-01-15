def is_possible(number, broken_buttons): #리모컨으로 누를수 있는지
    for digit in str(number):
        if int(digit) in broken_buttons:
            return False
    return True

def press_button(channel, broken_buttons):
    count = abs(channel - 100)  # 초기값: 현재 채널에서 100번 채널로 이동하는 횟수, +냐 - 계속 누르는거

    for i in range(1000001):  # 0부터 100만까지의 범위에서 채널을 찾음 => 999999 에서 뺴는 경우가 있음
        if is_possible(i, broken_buttons):
            count = min(count, abs(channel - i) + len(str(i)))  # 현재까지의 최소 횟수 갱신
        

    return count


N = int(input())
M = int(input())

if M > 0:
    broken_buttons = set(map(int, input().split()))
else:
    broken_buttons = set()

result = press_button(N, broken_buttons)
print(result)
