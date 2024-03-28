def binary_search(start, end, val, arr_sort):
    """
    이진 탐색 함수
    :param start: 시작 인덱스
    :param end: 끝 인덱스
    :param val: 찾을 값
    :param arr_sort: 정렬된 배열
    :return: 찾은 값의 인덱스 또는 가장 가까운 큰 값의 인덱스
    """
    while start < end:
        mid = (start + end) // 2
        if arr_sort[mid] > val:
            end = mid - 1
        elif arr_sort[mid] < val:
            start = mid + 1
        else:
            return mid
    return start

# 메인 함수
def main():
    ans = 3  # 최대 경우의 수
    N = int(input())  # 배열 크기 입력

    arr = list(map(int, input().split()))  # 배열 입력
    arr_sort = sorted(arr)  # 배열을 정렬하여 정렬된 배열 생성

    chance = 2  # 기회 카운터
    idx = 0  # 현재 배열의 인덱스

    # 정렬된 배열을 확인하며 연속된 덩어리 개수를 세는 과정
    while chance:
        sorted_index = binary_search(0, N - 1, arr[idx], arr_sort)

        # 현재 배열과 정렬된 배열이 일치하는 동안 인덱스 증가
        while idx < N and sorted_index < N and arr[idx] == arr_sort[sorted_index]:
            idx += 1
            sorted_index += 1

        # 배열을 모두 확인했을 때
        if idx == N:
            break
        else:
            chance -= 1  # 기회 감소
            continue

    print(ans - chance)  # 결과 출력

# 메인 함수 호출
if __name__ == "__main__":
    main()
