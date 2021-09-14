import sys
sys.stdin = open("sample_input (merge).txt")
# 병합 함수
def merge(l, r):
    s = []
    i = j = 0
    # 각 인덱스가 모두 유효한 동안 계속 반복
    while i < len(l) and j < len(r):
        # 오른쪽게 크면 먼저 추가
        if l[i] < r[j]:
            s.append(l[i])
            i += 1
        else:
            s.append(r[j])
            j += 1
    # 둘중 하나가 먼저 다 사용되면 사용 덜된 나머지 전부 s 뒤쪽에 이어 붙이기
    if i < len(l):
        s += l[i: len(l)]
    else:
        s += r[j: len(r)]
    return s

def merge_sort(s):
    global cnt
    n = len(s)
    # 1개 이하일땐 더이상 쪼갤수 없음 종료조건
    if n <= 1:
        return s
    else:
        mid = n // 2
        l = merge_sort(s[0: mid])
        r = merge_sort(s[mid: n])
        # 왼쪽 마지막 수가 오른쪽 마지막보다 큰 경우 세기
        if l[-1] > r[-1]:
            cnt += 1
        return merge(l, r)

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr = merge_sort(arr)
    print('#{} {} {}'.format(tc, arr[n//2], cnt))
