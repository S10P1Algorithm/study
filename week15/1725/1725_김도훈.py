import sys
N = int(input())
histogram = []
for _ in range(N):
    i = int(sys.stdin.readline().strip())
    histogram.append(i)
            
stack = []
temp_ans = 0
for idx, height in enumerate(histogram):
    if stack == []: # stack에 없으면
        stack.append([idx, height]) # 무조건 때려넣어
    else:
        width = idx # 현재 값의 idx 저장
        while stack != [] and stack[-1][1] > height: # top 값이 height보다 클 시
            value = stack.pop()
            width = value[0] # 마지막 pop한 히스토그램 idx 갱신
            size = value[1] * (idx - value[0]) # 넓이 구하기
            if temp_ans < size: # 최댓값 갱신
                temp_ans = size
        stack.append([width, height])
for value in stack: # 스택에 남은 애들 전부 계산
    size = value[1] * (N - value[0]) # 기준은 길이 N으로
    if temp_ans < size:
        temp_ans = size

print(temp_ans)