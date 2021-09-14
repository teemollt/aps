import sys
sys.stdin = open("sample_input (hw1).txt")

# 가로글자에서 각 자리수를 인덱스로 하는 배열만들어서 순서대로 넣어주면 될듯...
def idx(x):
    # idx가 0~14 가능
    tmp = [[] for _ in range(15)]
    # x는 가로 문자열 , 문자열 길이만큼 반복문
    for i in range(len(x)):
        # 각 자리 인덱스에 집어넣기
        tmp[i] += x[i]
    return tmp

t = int(input())
for tc in range(1, t+1):
    # 배열 입력
    arr = [input() for _ in range(5)]
    # print(arr)
    # print("----------------")
    #  최대 15글자까지 받을 수 있으므로 세로 15줄까지 나올수있음
    rst = ""

    # 5줄 각각 idx에 넣고 돌려
    # for i in range(15):
    tmp_list = []
    arr2 = []
    for i in range(5):
        arr2.append(idx(arr[i]))
    # print(arr2)
    # 여기서 나온 tmp의 각 같은자리 리스트끼리 더해줘
    for i in range(15):
        for j in range(5):
            tmp_list += arr2[j][i]
    # print(tmp_list)
    rst = ""
    for i in tmp_list:
        rst += i

    print('#{} {}'.format(tc, rst))
