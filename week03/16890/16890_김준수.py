# 회사 이름을 정하는 게임
# N개의 글자
# 처음의 이름 ? * N
# 각자 사용할 N개의 문자를 정함
# 같은 문자 중복 가능
# 구사과 부터
# 각 턴, 물음표 하나를 고른 문자로 변경.
# 고른 문자는 재 사용 불가
# 모든 물음표가 문자로 바뀌면 종료.
# 특정 인덱스의 문자를 변경
# 구사과는 회사 이름 사전 순 가장 앞서게 만들고 싶어함.
# 작은 알파벳 앞에서부터 넣기 (작은 알파벳 부터 쓰기?)
# 큐트러버는 회사 이름 사전 순 가장 뒤에 오게 만들고 싶어함.
# 큰 알파벳 앞에서부터 넣기, 작은 알파벳 뒤에서부터 넣기 (큰 알파벳 부터 쓰기?)
# 1<=N<=300000
# 모든 문자열은 알파벳 소문자로만 이루어짐
# 구사과 -> 큐트러버
# 두사람이 창업한 회사의 이름을 출력
# abcdefghijklmnopqrstuvwxyz

# nine_apple = sorted(list(input()))
# cute_lover = sorted(list(input()), reverse=True)
# N = len(nine_apple)
# is_odd = N % 2 != 0
# ans = []
# k = 0
# l = 0
# for i in range(0, N//2):
#     ans.append(nine_apple[k])
#     ans.append(cute_lover[l])
#     k += 1
#     l += 1
# if is_odd:
#     ans.append(nine_apple[k])
# print(''.join(ans))

# 음 서로의 정보를 다 안다고 한다....
# bb, aa => ab가 되어야 함.
# 구사과 ~ 가장 작은 문자열 < 큐트러버 ~ 가장 큰 문자열 -> 제일 앞으로
# 만약에 반대거나 같으면 -> 가장 큰 걸 제일 뒤로
# 마찬가지로 ~~ 반대로도 같게..!

import sys
input = sys.stdin.readline
from collections import deque

nine_apple = sorted(list(input().rstrip()))
cute_lover = sorted(list(input().rstrip()), reverse=True)
N = len(nine_apple)

nine_apple = deque(nine_apple)
cute_lover = deque(cute_lover)

ans = ['']*N
left = 0
right = N-1
for i in range(N):
    if i%2 == 0:
        if cute_lover and cute_lover[0] <= nine_apple[0]:
            ans[right] = nine_apple.pop()
            right -= 1
        else:
            ans[left] = nine_apple.popleft()
            left += 1
    else:
        if nine_apple and nine_apple[0] >= cute_lover[0]:
            ans[right] = cute_lover.pop()
            right -= 1
        else:
            ans[left] = cute_lover.popleft()
            left += 1
print(''.join(ans))

# 모르겠다!!!
# 왜 조금씩 틀릴까용?????