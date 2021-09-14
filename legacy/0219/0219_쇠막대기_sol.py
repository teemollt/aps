t = int(input())
for tc in range(1, t+1):
    bar = input()
    # 쇠막대기 개수
    cnt = 0
    # 정답
    rst = 0

    for i in range(len(bar)):
        # 여는 괄호라면 막대 추가
        if bar[i] == '(':
            cnt += 1
        else:
            # 닫힌 괄호면 막대 감소
            # 레이저라면 잘못 넣은거니 빼고
            # 아니라면 어차피 철봉 끝이니 빼자
            cnt -= 1

            # 레이저라면
            if bar[i-1] == '(':
                # 레이저로 인해 잘린 막대들이 생겼으므로
                rst += cnt
            else:
                # 막대끝
                rst += 1
    print('#{} {}'.format(tc, rst))


###################################################################리스트 활용 풀이

for tc in range(1, t+1):
    bar = input()
     # 실제 철봉이 담길 릴스트
    s = []
    ans = 0

    for i in range(len(bar)):
        # 열린괄호라면 s리스트에 넣어놓기
        if bar[i] == '('
            s.append('(')
        else:
            # 무조건 꺼내기
            s.pop()

            if bar[i-1] == '(':
                ans += len(s)
            else:
                ans += 1
    print('#{} {}'.format(tc, ans))