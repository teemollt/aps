# import sys
# sys.stdin = open("sample_input (4869).txt")
t = int(input())
for tc in range(1, t+1):
    # 어차피 10의 배수로 주어지므로 입력값에 10을 나누어 사용
    n = int(input()) // 10
    # 길이가 n일때 까지 값을 담아야하므로 n+1까지 배열을 만들어놓음
    cnt = [0] * (n+1)
    # 길이가 0일때 1로 초기화
    cnt[0] = 1
    # 길이가 1일때 1가지 방법 뿐이므로 1
    cnt[1] = 1
    # 종이를 붙이는 경우의수가 이전 길이의 경우의수 + 전전 길이일때 경우의수 *2 이므로
    for i in range(2, n+1):
        cnt[i] = cnt[i-1] + cnt[i-2]*2

    print('#{} {}'.format(tc, cnt[n]))