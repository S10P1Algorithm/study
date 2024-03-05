import sys

Land = [[0] * 20 for _ in range(20)]
dice = [0, 0, 0, 0, 0, 0]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

command = [
    [
        [1, 4, 2, 3],
        [2, 3, 4, 1],
        [3, 2, 1, 4],
        [4, 1, 3, 2]
    ],
    [
        [3, 2, 5, 0],
        [5, 0, 2, 3],
        [0, 5, 3, 2],
        [2, 3, 0, 5]
    ],
    [
        [1, 4, 5, 0],
        [4, 1, 0, 5],
        [5, 0, 4, 1],
        [0, 5, 1, 4]
    ],
    [
        [5, 0, 1, 4],
        [0, 5, 4, 1],
        [1, 4, 0, 5],
        [4, 1, 5, 0]
    ],
    [
        [0, 5, 2, 3],
        [2, 3, 5, 0],
        [5, 0, 3, 2],
        [3, 2, 0, 5]
    ],
    [
        [3, 2, 4, 1],
        [4, 1, 2, 3],
        [1, 4, 3, 2],
        [2, 3, 1, 4]
    ]
]


def main():
    global Land, dice
    # sys.stdin = open("14499.txt", "r")
    N, M, x, y, K = map(int, input().split())

    for i in range(N):
        Land[i] = list(map(int, input().split()))

    diceFace = 0
    next_command = command[0][2]
    for _ in range(K):
        cmd = int(input()) - 1

        nx = x + dx[cmd]
        ny = y + dy[cmd]

        if 0 <= nx < N and 0 <= ny < M:
            x = nx
            y = ny
            nextDiceFace = next_command[cmd]
            thisDiceFaceWillbeAt = cmd - 1 if cmd % 2 else cmd + 1

            for i in range(4):
                if command[nextDiceFace][i][thisDiceFaceWillbeAt] == diceFace:
                    next_command = command[nextDiceFace][i]
                    break
            diceFace = nextDiceFace

            if Land[nx][ny]:
                dice[diceFace] = Land[nx][ny]
                Land[nx][ny] = 0
            else:
                Land[nx][ny] = dice[diceFace]

            print(dice[5 - diceFace])

if __name__ == "__main__":
    main()
