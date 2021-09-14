import sys
sys.stdin = open("sample_input (hh).txt")
t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    num = list(map(int, input().split()))
    for i in range(m):
        num.append(num.pop(0))
    print('#{} {}'.format(tc, num[0]))