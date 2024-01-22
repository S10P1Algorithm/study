# N개의 서로 다른 정수
# 1. k개의 조각으로 자른다. 2. k개의 조각을 원하는 순서대로 재배열 3. 재배열한 순서대로 다시 합친다.
# 원하는 횟수만큼 적용 (0번도 ㄱㅊ) -> 오름차순
# 적용할 수 있는 방법이 없을 수도 있음
# 정렬할 수 있는 가장 작은 양의 정수 k의 값을 구한다.
n = int(input())
arr = list(map(int, input().split()))

cnt = 0 # 순서가 맞지 않는 수
arr.insert(0, -1) # 비교를 위해서 insert
is_sorted = True # 이미 정렬되어있는지
flag = True #

for i in range(1, n + 1):
    # 정렬되어 있는지
    if arr[i] < arr[i - 1]:
        is_sorted = False
        cnt += 1
    # 두 그룹으로 나누었을 때, 정렬이 가능한지
    if cnt and arr[i] > arr[1]:
        flag = False

if is_sorted:
    print(1)
# 두 그룹으로 정렬되어있음 (한번에 가능 cnt == 1)
elif cnt == 1 and flag:
    print(2)
else:
    print(3)
