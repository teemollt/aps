import sys
sys.stdin = open("sample_input (2).txt")
T = int(input())

# 0~9까지 카드가 있으므로 0~9 인덱스를 가지는 리스트를 만들어서 카드 개수를 요소로 넣으면 될듯
for tc in range(1, T+1):
    # N : 카드의 개수
    N = int(input())
    card = input()

    # 배열 생성
    cnt = [0] * 10

    max_cnt = -1
    max_num = -1

    # 카드 숫자 세기
    for i in card:
        cnt[int(i)] += 1

    for i in range(len(cnt)):
        if max_cnt <= cnt[i]:
            max_num = i
            max_cnt = cnt[i]

    print('#{} {} {}'.format(tc, max_num, max_cnt))

###########################풀이 2##########################
T = int(input())

# 0~9까지 카드가 있으므로 0~9 인덱스를 가지는 리스트를 만들어서 카드 개수를 요소로 넣으면 될듯
for tc in range(1, T+1):
    # N : 카드의 개수
    N = int(input())
    card = input()

    # 배열 생성
    cnt = [0] * 10

    max_cnt = -1
    max_num = -1

    # 카드 숫자 세기 동시에 제일 많은 숫자 찾기
    for i in card:
        cnt[int(i)] += 1
        if max_cnt <= cnt[i]:
            max_num = i
            max_cnt = cnt[i]
    # 그리고 제일 뒤부터 반복문 돌리면서 같은 장수의 idx를 찾으면 그대로 cnt에 넣고 break 그게 가장 많은 장수중 젤 큰 idx니까
    # 반복문 도는 방향 + break 활용하는 방식 생각해봐... 의미
    for i in range(len(cnt) - 1, -1, -1):
        if max_cnt == cnt[i]:
            max_num = i
            break

    print('#{} {} {}'.format(tc, max_num, max_cnt))