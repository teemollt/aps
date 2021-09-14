import sys
sys.stdin = open("sample_input (2).txt")
def countt(s):
    cnt = 0
    for i in s:
        cnt += 1
    return cnt

def summ(s):
    total = 0
    for i in s:
        total += i
    return total

t = int(input())
for tc in range(1, t+1):
    # 집합 a(1~12)
    a = [i for i in range(1, 13)]
    # 부분집합 원소의수 n , 합 k
    n, k = map(int, input().split())
    # 부분집합
    rst = 0
    for i in range(1<<len(a)):
        p = []
        for j in range(len(a)+1):
            # j번째 비트가 1인지 확인
            if i & (1<<j):
                p.append(a[j])
        # n, k에 부합하는지 검사
        if countt(p) == n and summ(p) == k:
            rst += 1

    print('#{} {}'.format(tc, rst))
