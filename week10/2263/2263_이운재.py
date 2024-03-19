import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

# inorder의 값 index 리스트
inorder_index = [0] * (n + 1)
for i in range(n):
    inorder_index[inorder[i]] = i


# inorder의 시작 인덱스, 끝 인덱스/postorder의 시작 인덱스, 끝 인덱스
def preorder(in_start, in_end, post_start, post_end):
    global inorder, postorder
    # 재귀 종료 조건
    if in_start > in_end or post_start > post_end:
        return

    # 현 트리에서 최상위 루트
    root = postorder[post_end]
    print(root, end=' ')

    # inorder에서 root 위치 찾기
    in_root = inorder_index[root]
    # 왼쪽 서브트리
    # 왼쪽 서브트리 노드의 개수
    left = in_root - in_start
    preorder(in_start, in_root - 1, post_start, post_start + left - 1)
    # 오른쪽 서브트리
    # 오른쪽 서브트리 노드의 개수
    right = in_end - in_root
    preorder(in_root + 1, in_end, post_end - right, post_end - 1)


preorder(0, n - 1, 0, n - 1)