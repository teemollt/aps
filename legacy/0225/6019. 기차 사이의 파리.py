import sys
sys.stdin = open("s_input.txt")
t = int(input())
for tc in range(1, t+1):
    # 두 기차 사이 거리 d, a기차의 속력, b기차의 속력, f파리속력
    D, A, B, F = map(int, input().split())
