import sys
sys.stdin = open("sample_input (4880).txt")

# 분할정복!!

# 그룹을 두개로 나누어서 승자 뽑기
# 그룹이 2명으로 이루어지거나 또는 한명으로 이루어 질때까지
# 그룹을 나누어 주고, 각각의 승자를 뽑아야한다.

# 하나의 그룹을 두 그룹으로 나누어서
# 각각의 승자 중 승자의 번호를 반환하는 함수
def game(s, e):
    # 전체 그룹을 두그룹으로 나누고
    # 각 절반의 승자를 뽑아서
    # 승자끼리 결과를 반환
    # 그룹에 포함되는 학생이 1명이면 재귀 호출 중단
    if s == e:  # s == e 면 그룹에 포함되는 학생이 1명
        # 승자는 스스로가 됨.
        return s

    center = (s+e) // 2
    v1 = game(s, center)
    v2 = game(center+1, e)
    # v1과 v2중에 승자 뽑기
    if cards[v1] == '1':        # v1이 가위인 상황
        if cards[v2] == '2':
            return v2
        else:
            return v1
    elif cards[v1] == '2':   # v1이 바위
        if cards[v2] == '3':
            return v2
        else:
            return v1
    else:
        if cards[v2] == '1':
            return v2
        else:
            return v1

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    cards = input().split()
    # 학생번호 1~n 까지 인데 인덱스는 0~n-1 까지니까
    # 결과 출력할때 승자번호 +1 해주면됨
    rst = game(0, n-1)
    print('#{} {}'.format(tc, rst+1))