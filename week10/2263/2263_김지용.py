import sys

input = sys.stdin.readline

n = int(input())

inorder_input = list(map(int, input().split()))
postorder_input = list(map(int, input().split()))

root = postorder_input[-1]



