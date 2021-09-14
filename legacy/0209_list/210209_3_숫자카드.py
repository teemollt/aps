import sys
sys.stdin = open("sample_input (2).txt")
T = int(input())

# 0~9까지 카드가 있으므로 0~9 인덱스를 가지는 리스트를 만들어서 카드 개수를 요소로 넣으면 될듯
for tc in range(1, T+1):
    N = int(input())
    card = input()
    card_list = [0] * 10
    # 반복문으로 각 요소에
    for i in range(len(card)):
        card_list[int(card[i])] += 1
    num_cnt = 0
    num_idx = 0
    for j in range(len(card_list)):
        if card_list[j] > num_cnt:
            num_cnt = card_list[j]
            num_idx = j
        elif card_list[j] == num_cnt:
            num_idx = j
    print('#{} {} {}'.format(tc, num_idx, num_cnt))



