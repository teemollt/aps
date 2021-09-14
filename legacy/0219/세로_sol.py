import sys
sys.stdin = open("sample_input (hw1).txt")

t = int(input())

for tc in range(1, t+1):
    word = [0] * 5
    max_len = 0

    for i in range(5):
        word[i] = list(input())

        # 입력 받으면서 최대길이 갱신
        if len(word[i]) > max_len:
            max_len = len(word[i])

    # 세로로 읽어보자.

    print('#{}'.format(tc), end=" ")
    for i in range(max_len):
        for j in range(5):
            # if len(word[j]) > i:
            #     print(word[j][i], end="")
            try:
                print(word[j][i], end="")
            except:
                pass
            # try / except는 안쓰는게 좋음... 조건문으로 풀자
    print()
