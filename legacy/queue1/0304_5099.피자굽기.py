import sys
sys.stdin = open("sample_input (pizza).txt")

t = int(input())
for tc in range(1, t+1):
    # n개 피자 동시에 굽굽, 1~~m번까지 m개의 피자를 순서대로 화덕에 넣음
    n, m = map(int, input().split())
    # 뿌려진 치즈의 양 c , 치즈는 꺼낼때마다 c//2로 줄어듬
    c = list(map(int, input().split()))
    # 화덕 q에 피자 m개 순서대로 넣기 화덕의 크기는 n
    q = []
    for i in range(m):
        # 화덕이 가득찰때까지 피자 넣고 가득차면 순서대로 꺼내보기 하나가 빠질때까지
        q.append((c[i], i+1))
        if len(q) == n:
            while len(q) == n:
                # 처음 넣은 피자 치즈 녹이고
                pizza = q.pop(0)
                # 확인했을때 치즈가 0이 아니면 다시 추가
                if pizza[0]//2 > 0:
                    q.append((pizza[0]//2, pizza[1]))
                else:
                    break
    # 이제 주어진 피자 화덕에 다 들어갔으니 화덕에 피자가 1개 남을때까지 실행
    while len(q) > 1:
        # 처음 넣은 피자 치즈 녹이고
        pizza = q.pop(0)
        # 확인했을때 치즈가 0이 아니면 다시 추가
        if pizza[0] > 0:
            q.append((pizza[0] // 2, pizza[1]))
    # 하나남은 피자 번호 확인
    rst = q[0][1]
    print('#{} {}'.format(tc, rst))

