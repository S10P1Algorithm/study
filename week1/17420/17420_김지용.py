import sys

input = sys.stdin.readline

N = int(input())

remaining = list(map(int, input().split()))
plan = list(map(int, input().split()))

sorted_plan = sorted(zip(remaining, plan))