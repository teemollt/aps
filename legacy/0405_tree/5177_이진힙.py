import sys
sys.stdin = open("sample_input (h).txt")
# N개의 서로 다른 자연수가 주어지면 입력 순서대로 이진 최소힙에 저장하고,
# 마지막 노드의 조상 노드에 저장된 정수의 합을 알아내는 프로그램을 작성
def sol(v):
    global tree
    # 왼쪽확인
    if 0 < v < len(tree) and v*2 < len(tree):
        sol(v*2)
    # 더 못가면 나오고 부모랑 비교
    # 자식이 항상 더 커야됨
    if tree[v] < tree[v//2]:
        # 아니면 바꿔주기
        tmp = tree[v]
        tree[v] = tree[v//2]
        tree[v//2] = tmp

    # 오른쪽도
    if 0 < v < len(tree) and v*2+1 < len(tree):
        sol((v * 2)+1)


t = int(input())
for tc in range(1, t+1):
    # n개의 자연수
    n = int(input())
    # 주어지는 자연수들..
    data = list(map(int, input().split()))
    tree = [0]
    # 하나씩 넣기
    for i in range(n):
        tree.append(data[i])
        # 추가할때마다 크기 비교
        sol(1)

    # 마지막 노드 idx
    idx = len(tree) - 1
    # idx가 0보다 큰동안 반복
    rst = 0
    while idx > 0:
        # 부모 idx 찾아서
        idx //= 2
        # 더해주기
        rst += tree[idx]

    print('#{} {}'.format(tc, rst))
