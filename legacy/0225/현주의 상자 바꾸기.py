import sys
sys.stdin = open("sample_input (box).txt")
t = int(input())
for tc in range(1, t+1):
    # (1~Q) i 번째 작업 L ~ R 상자 값을 i로 변경 Q회 동안 N개의 상자에 적혀있는 값 순서대로 출력
    N, Q = map(int, input().split())
    # 기본 상자
    box = ['0']*(N+1)
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L, R+1):
            box[j] = str(i)

    box = box[1::]

    print('#{} {}'.format(tc, " ".join(box)))

    # for i in range(1, N+1):
    #     print(box[i], end=" ")

