import sys
sys.stdin = open("input (7).txt")

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    code = [list(input().split()) for _ in range(n)]
    print(code)
