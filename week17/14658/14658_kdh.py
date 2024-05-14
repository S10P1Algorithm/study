import sys
sys.stdin = open("input.txt", "r")

N, M, L, K = map(int, input().split())
meteor = []
for _ in range(K):
    x, y = map(int, input().split())
    meteor.append((x, y))

def max_points_in_square(N, M, L, K, points):
    # 점들을 x 좌표 순으로 정렬
    points.sort()
    
    max_count = 0
    # y 좌표로 점들을 관리할 리스트
    y_points = []
    
    # 슬라이딩 윈도우 사용
    left = 0
    for right in range(K):
        # 정사각형 범위 내에 들어오는 y좌표를 리스트에 추가
        while points[right][0] - points[left][0] > L:
            left += 1
        # 현재 right 포인트를 정사각형의 왼쪽 끝으로 간주하고 y 범위를 정한다
        current_x = points[right][0]
        y_range = []
        for i in range(left, right + 1):
            if points[i][1] <= points[right][1] + L:
                y_range.append(points[i][1])
        
        # y 좌표를 정렬하여 슬라이딩 윈도우 처리
        y_range.sort()
        y_left = 0
        for y_right in range(len(y_range)):
            while y_range[y_right] - y_range[y_left] > L:
                y_left += 1
            max_count = max(max_count, y_right - y_left + 1)
    
    return max_count

print(K-max_points_in_square(N, M, L, K, meteor))