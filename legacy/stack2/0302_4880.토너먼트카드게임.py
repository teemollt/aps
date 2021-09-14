import sys
sys.stdin = open("sample_input (4880).txt")


def div(s1, e1, s2, e2):
    e1 = (s1+e1)//2
    s2 = (s2+e2)//2 + 1
    if s1 == e1:
        return s1
    if s2 == e2:
        return s2
    else:
        div(s1, e1, s2, e2)





t = int(input())
for tc in range(1, t+1):
    # n 명
    n = int(input())
    # 카드 번호 1은 가위, 2는 바위, 3은 보
    card = input().split()
    # print(n, card)
    # 두그룹으로 1대1 될때까지 나눠서 카드번호 리턴
    # print(div(0, 8))


