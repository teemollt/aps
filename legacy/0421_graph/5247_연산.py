import sys
sys.stdin = open("sample_input (cal).txt")

def sol(num, cnt):
    global used, q
    front = 0
    rear = 0
    q[rear] = (num, cnt)
    rear += 1
    used[num] = 1
    while front != rear:
        N, C = q[front]
        front += 1
        tmp = [N*2, N-10, N+1, N-1]
        for i in range(4):
            if tmp[i] == m:
                return C+1
            elif 0 < tmp[i] <= 1000000 and not used[tmp[i]]:
                q[rear] = (tmp[i], C + 1)
                rear += 1
                used[tmp[i]] = 1

t = int(input())
for tc in range(1, t+1):
    # 자연수 n으로 m만들기
    n, m = map(int, input().split())
    used = [0]*1000001
    q = [0]*2000000
    print('#{} {}'.format(tc, sol(n, 0)))