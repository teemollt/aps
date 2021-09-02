import sys
input = sys.stdin.readline
t = int(input())
for tc in range(t):
    v, e = map(int, input().rstrip().split())
    arr = [[] for _ in range(v+1)]

