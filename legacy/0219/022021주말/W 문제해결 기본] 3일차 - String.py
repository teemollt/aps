import sys
sys.stdin = open("test_input(string).txt", 'rt', encoding='UTF8')

t = 10
for tc in range(1, t+1):
    tn = int(input())
    word = input()
    sen = input()
    le = len(word)
    cnt = 0
    for i in range(len(sen)-le+1):
        tmp = ""
        tmp2 = ""
        for j in range(le):
            tmp += sen[i+j]
            tmp2 += word[j]
        if tmp == tmp2:
            cnt += 1

    print('#{} {}'.format(tc, cnt))
