import sys
sys.stdin = open("sample_input.txt")
T = int(input())
for tc in range(1, T+1):
    # 입력
    N = int(input())
    numbers = list(map(int, input().split()))
    # 차이가 가장 작을 경우 0이므로 0으로 초기화
    rst = 0
    # 반복문으로 큰수/작은수 구하기
    # 각각 담을 변수
    max_v = numbers[0]
    min_v = numbers[0]
    for i in numbers:
        if max_v < i:
            max_v = i
        if min_v > i:
            min_v = i

    rst = max_v - min_v
    print('#{} {}'.format(tc, rst))