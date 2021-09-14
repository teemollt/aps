import sys
sys.stdin = open("input (cal).txt")

def sol(v):
    global tree
    if left[v]:
        sol(left[v])
    if right[v]:
        sol(right[v])
    if tree[v] == '+':
        tree[v] = tree[left[v]] + tree[right[v]]
    elif tree[v] == '-':
        tree[v] = tree[left[v]] - tree[right[v]]
    elif tree[v] == '*':
        tree[v] = tree[left[v]] * tree[right[v]]
    elif tree[v] == '/':
        tree[v] = tree[left[v]] / tree[right[v]]

for tc in range(1, 11):
    # 정점의 총수 n
    n = int(input())
    # 노드가 정수면 정점번호 정수
    # 연산자면 정점번호 연산자 왼쪽자식 오른쪽자식
    tree = [0] * 1001
    left = [0] * 1001
    right = [0] * 1001
    for i in range(n):
        data = input().split()
        # data 리스트 크기로 연산자인지 아닌지 구분
        if len(data) > 2:
            # 2보다 크면 연산자니까
            # tree에 해당 연산자 넣고
            tree[int(data[0])] = data[1]
            # 자식 노드번호 리스트에 담기
            left[int(data[0])] = int(data[2])
            right[int(data[0])] = int(data[3])
        # 해당 노드의 값이 정수일 경우
        else:
            # 그냥 해당 노드에 정수넣기
            tree[int(data[0])] = int(data[1])
    sol(1)
    print('#{} {}'.format(tc, int(tree[1])))
