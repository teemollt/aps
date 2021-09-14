import sys
from itertools import permutations
sys.stdin = open("sample_input (베이비진).txt")

# 조합
# d 깊이, s 시작점, n 전체 개수, 뽑는 개수 3, 주어지는 배열 a

def check(arr):
    global win
    # arr.sort()
    if arr[0] == arr[1] == arr[2]:
        win = 1
    if arr[0]+1 == arr[1] and arr[1]+1 == arr[2]:
        win = 1
    if arr[0] == 0 and arr[1] == 8 and arr[2] == 9:
        win = 1
    if arr[0] == 0 and arr[1] == 1 and arr[2] == 9:
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
        # 3개 이상일때 조합
        n = len(p1)
        c1 = []
        if n >= 3:
            a = list(permutations(p1, 3))
            for j in a:
                check(j)
            # print(a)
        if win:
            rst = 1
            break
        m = len(p2)
        p2.append(cards[i+1])
        if m >= 3:
            b = permutations(p2, 3)
            for j in b:
                check(j)
        if win:
            rst = 2
            break
    print('#{} {}'.format(tc, rst))