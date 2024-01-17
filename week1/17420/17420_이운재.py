'''
1. 기한 연장을 최소한으로 하고 싶어한다.
2. 남은 기프티콘 중 기한이 가장 적게 남은 기프티콘만 사용할 수 있다.
3. 단 기한이 가장 적게 남은 기프티콘이 여러 개라면 그 중 아무거나 선택할 수 있다.
4. 하루에 여러 기프티콘을 사용하거나 연장하는 것 모두 가능하다.
5. 한번 연장에 30일이 늘어난다.

원하는 것 - 최소 횟수로 기한 연장을 하면서 기프티콘을 다 쓸 수 있도록 정우를 도와주자.

첫째 줄에 기프티콘의 수 N이 주어진다.

둘째 줄에 A1, A2, ..., AN가 주어진다. 이는 i번째 기프티콘의 남은 기한이 Ai일이라는 뜻이다.

셋째 줄에 B1, B2, ..., BN가 주어진다. 이는 i번째 기프티콘을 Bi일 뒤에 사용할 계획이라는 뜻이다.
------------------------------------------------------------------------------

첫째 줄에 정우가 기한 연장을 해야 하는 최소 횟수를 출력한다.
'''

'''
문제 포인트 : 예를 들어 30일 이후의 쓸 기프티콘이, 35일 이후의 쓸 기프티콘 보다 늦게 사용하면 안된다.
정렬 을 하고 난뒤 이전 기프티콘 보다 무조건 남은 기한이 많아야 한다.
'''
import sys

input = sys.stdin.readline

N = int(input())

rested = list(map(int,input().split()))
will_use = list(map(int,input().split()))

# for i in range(N):
#     if will_use[i] > rested[i]:
#         share, remainder= divmod((will_use[i] - rested[i]), 30)
#         answer += share
#         print(share,remainder)
#         if remainder > 0:
#             answer += 1

# print(answer)
            
arr = []

for i in range(N):
    arr.append([rested[i],will_use[i]])

# 사용 계획일을 먼저 정렬하고, 남은 기한에 따라 또 정렬을 해준다. 
arr.sort(key= lambda x: (x[1],x[0]))

# 첫번째 사용계획값 설정 
prev = arr[0][1]

# 정렬후 이전 인덱스 보다 남은 기한이 높아야, 사용 계획에 위반하지 않고 사용 가능
nowmax = 0

# 출력 값
result = 0

# 기한연장을 몇번 더해줄지에 대한 값
cnt = 0
for i in range(N):
    if prev > arr[i][0]: # 사용 계획이 남은 기한 보다 많으면

        # 사용 계획의 값을 계속 갱신 -> 그래야 기한 연장을 얼만큼 할지 판별 가능
        prev = max(prev, arr[i][1])

        # 기한 연장을 몇번 할지에 대한 값 구하기. 사용계획일에서 남은기한을 뺴고, 30으로 나눈 몫과 나머지를 구해준다
        share,remained = divmod((prev - arr[i][0]), 30)

        # 몫을 더해주고, 나머지가 0보다 크면 + 1을 해준다
        cnt = share
        if remained > 0:
            cnt += 1
        arr[i][0] += cnt * 30 # 기한 연장,
        result += cnt

    # 이걸 하는 이유는 이전 기프티콘 보다 나중을 쓰기 위해, 남은 기한이 무조건 이전 기프티콘 보다 높아야하기 때문이다.
    nowmax = max(nowmax, arr[i][0])

    # 정렬을 하고 난뒤 이전 기프티콘하고 사용 계획 일자가 다를 경우 갱신 해줘야 한다.
    if i + 1 < N and (arr[i][1] != arr[i+1][1]):
        prev = nowmax

print(result)
         



