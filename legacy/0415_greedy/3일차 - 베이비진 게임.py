import sys
from itertools import combinations
sys.stdin = open("sample_input (베이비진).txt")

# 전체 순열..
# 조합으로 하는게 좋은데 조합이 잘안됨....
def perm(idx, d, a):
    global arr, used
    # 종료조건
    if d == 3:
        check(arr)
        # x = sorted(arr)
        # print(x)
        return
    for i in range(n):
        if used[i] == 0:
            arr[d] = a[i]
            used[i] = 1
            perm(idx+1, d+1, a)
            used[i] = 0
    # for i in range(s, n-3+d+1):
    #     arr[d] = a[i]
    #     comb(d+1, i+1, n, a)

def check(arr):
    global win
    # arr.sort()
    if arr[0] == arr[1] == arr[2]:
        win = 1
    if arr[0]+1 == arr[1] and arr[1]+1 == arr[2]:
        win = 1

t = int(input())
for tc in range(1, t+1):
    # 0부터 9까지인 숫자 카드 4세트를 섞은 후 6개의 카드를 골라
    # 연속인 숫자가 3개 이상이면 run, 같은 숫자가 3개 이상이면 triplet
    # 교대로 한 장 씩 카드를 가져가며, 6장을 채우기 전이라도 먼저 run이나 triplet이 되는 사람이 승자
    # 승자를 알아내는 프로그램을 작성하시오. 만약 무승부인 경우 0을 출력
    cards = list(map(int, input().split()))
    p1 = []
    p2 = []
    win = 0
    rst = 0
    for i in range(0, 11, 2):
        p1.append(cards[i])
        # 3개 이상일때
        n = len(p1)
        c1 = []
        if n >= 3:
            arr = [0] * 3
            used = [0] * n
            perm(0, 0, p1)
        if win:
            rst = 1
            break
        m = len(p2)
        p2.append(cards[i+1])
        if m >= 3:
            arr = [0] * 3
            used = [0] * n
            perm(0, 0, p2)
        if win:
            rst = 2
            break
    print('#{} {}'.format(tc, rst))