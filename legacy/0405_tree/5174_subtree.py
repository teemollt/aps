import sys
sys.stdin = open("sample_input (subtree).txt")

def sol(v):
    global cnt
    if ch1[v]:
        sol(ch1[v])
    cnt += 1
    if ch2[v]:
        sol(ch2[v])

t = int(input())
for tc in range(1, t+1):
    # 간선의 개수 e <= 1000, 구해야할 서브트리 루트 노드n
    e, n = map(int, input().split())
    # 2 1 2 5 1 6 5 3 6 4
    # 노드의 최대 번호는 e+1 번 이므로 e+1까지 배열 만들기
    ch1 = [0] * (e+2)
    # 이진트리니까 두개
    ch2 = [0] * (e+2)
    data = list(map(int, input().split()))
    for i in range(0, 2*e, 2):
        # 자식리스트1이 비어있으면 넣어주기
        if not ch1[data[i]]:
            ch1[data[i]] = data[i+1]
        # 자식리스트1이 비어있지 않고 2가 비어있으면
        elif not ch2[data[i]]:
            ch2[data[i]] = data[i+1]
    cnt = 0
    sol(n)
    print('#{} {}'.format(tc, cnt))

