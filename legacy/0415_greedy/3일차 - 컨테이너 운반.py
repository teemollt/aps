import sys
sys.stdin = open('sample_input (컨테이너).txt')

def sol(idx):
    global sp, sw, uw, up, sum_w
    if idx == len(w):
        return
    for i in range(len(p)):
        if sw[idx] <= sp[i] and not up[i]:
            up[i] = 1
            sum_w += sw[idx]
            uw[idx] = 1
            sol(idx+1)
            break
    if idx < len(w)-1 and not uw[idx+1]:
        sol(idx+1)

t = int(input())
for tc in range(1, t+1):
    # 컨테이너수 n, 트럭수 m
    n, m = map(int, input().split())
    # n개의 화물 무게 리스트
    w = list(map(int, input().split()))
    # m개의 트럭 적재용량 리스트
    p = list(map(int, input().split()))
    # 트럭당 한 개의 컨테이너를 운반 할 수 있고, A도시에서 B도시로 최대 M대의 트럭이 편도
    # 이동한 화물의 총 중량이 최대가 되도록 컨테이너를 옮겼다면, 옮겨진 화물의 전체 무게가 얼마인지
    # 화물 무게 무거운 순으로 정렬 무조건 무거운걸 옮길수록 총량이 up
    sw = sorted(w, reverse=True)
    # 화물차도 적재용량 무거운순 정렬
    sp = sorted(p, reverse=True)
    uw = [0] * len(w)
    up = [0] * len(p)
    sum_w = 0
    idx = 0
    sol(0)
    print('#{} {}'.format(tc, sum_w))



