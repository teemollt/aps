import sys
sys.stdin = open("input (3pw).txt")

def sol(x):
    # 맨뒤로 보낸 숫자가 0보다 작아지면 반복 종료 그 숫자는 0으로
    while x[-1] > 0:
        # 1사이클 돌기
        for i in range(1, 6):
            # 반복 돌면서 리스트의 마지막이 0이하면 0으로 만들고 break해주기
            if x[-1] <= 0:
                x[-1] = 0
                break
            # 아니면 사이클 계속 돌자
            else:
                # 0번째 pop해주고 i만큼 빼주고 append
                x.append(x.pop(0) - i)
    x[-1] = 0
    return x

for _ in range(10):
    tc = int(input())
    data = list(map(int, input().split()))
    print('#{}'.format(tc), end=" ")
    for i in range(8):
        print(sol(data)[i], end=" ")
    print()

