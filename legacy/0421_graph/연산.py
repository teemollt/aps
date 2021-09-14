import sys
from collections import deque
sys.stdin = open("sample_input (cal).txt")

def sol(num, cnt):
    global used
    q = deque()
    q.append((num, cnt))
    used[num] = 1
    while q:
        N, C = q.popleft()
        # if N == m:
        #     return C
        tmp = [N*2, N-10, N+1, N-1]
        for i in range(4):
            if tmp[i] == m:
                return C+1
            elif 1 <= tmp[i] <= 1000000 and not used[tmp[i]]:
                q.append((tmp[i], C + 1))
                used[tmp[i]] = 1

t = int(input())
for tc in range(1, t+1):
    # 자연수 n으로 m만들기
    n, m = map(int, input().split())
    used = [0]*2000000
    print('#{} {}'.format(tc, sol(n, 0)))