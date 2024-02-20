from itertools import combinations

def simulate(board, archer_positions, N, M, D):
    # 복사된 보드를 생성하여 게임 진행
    board = [row[:] for row in board]
    enemies = 0
    
    # 아래 방향으로 적을 이동시키는 함수
    def move_enemies(board):
        new_board = [[0] * M for _ in range(N)]
        for r in range(N-2, -1, -1): # 맨 아랫줄은 확인할 필요 없음
            for c in range(M):
                if board[r][c] == 1:
                    new_board[r+1][c] = 1
        return new_board
    
    # 적을 제거하는 함수
    def attack(board, archer_positions):
        targets = set() # 공격 대상 적의 위치를 저장할 집합
        for archer in archer_positions:
            min_dist = float('inf') # 가장 가까운 적의 거리
            target = None # 가장 가까운 적의 위치
            for r in range(N-1, -1, -1): # 행의 역순으로 탐색
                for c in range(M):
                    if board[r][c] == 1:
                        dist = abs(N - r) + abs(archer - c)
                        if dist <= D and dist < min_dist:
                            min_dist = dist
                            target = (r, c)
                            # 거리가 같을 경우 왼쪽에 있는 적을 선택
                        elif dist == min_dist and c < target[1]:
                            target = (r, c)
            if target:
                targets.add(target)
        # 공격 대상 적 제거
        for target in targets:
            r, c = target
            board[r][c] = 0
        return len(targets)
    
    # 게임을 진행하면서 궁수의 공격으로 제거한 적의 수를 센다.
    for _ in range(N):
        enemies += attack(board, archer_positions)
        board = move_enemies(board)
    
    return enemies

def solution(N, M, D, board):
    max_enemies = 0
    # 궁수 배치 가능한 열에 대한 모든 조합을 생성
    for positions in combinations(range(M), 3):
        max_enemies = max(max_enemies, simulate(board, positions, N, M, D))
    return max_enemies

# 입력 받기
N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 결과 출력
print(solution(N, M, D, board))
