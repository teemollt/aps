import sys
sys.stdin = open("sample_input (4880).txt")
# 이제야 제대로 이해하고 풀어서 늦게 제출합니당...
def sol(s, e):
    # 두그룹으로 나누기
    # 가운데
    mid = (s+e)//2
    # 한개만 남았으면(l이랑 r이랑 같으면 한개 남은거) 옆이랑 비교해서 이긴사람 올리기
    if s == e:
        return (card[s-1], s)
    # 왼쪽그룹 오른쪽그룹
    l = sol(s, mid)
    r = sol(mid+1, e)
    # l,r 가위바위보 1은 가위, 2는 바위, 3은 보
    # l이 올라가는 경우
    if (l[0] == r[0]) or (l[0] == '1' and r[0] == '3') or (l[0] == '2' and r[0] == '1') or (l[0] == '3' and r[0] == '2'):
        return l
    else:
        return r

t = int(input())
for tc in range(1, t+1):
    # n명
    n = int(input())
    # n명이 고른 카드번호 순서대로
    card = input().split()
    print('#{} {}'.format(tc, sol(1, n)[1]))
