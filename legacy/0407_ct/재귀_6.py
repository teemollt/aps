# 노드번호, 값, 자식 노드번호들. 입력
# 다른 값도 넣어보면 출력 위치가 약간 깨지긴하지만 작동이 되긴함..
numbers = [[0], [1, '030', 2, 3, 4], [2, '054', 5], [3, '002'], [4, '045', 6], [5, '001'], [6, '123']]
# 빈리스트 트리 주어지는 노드 개수+1
tree = [0] * (len(numbers)+1)
def sol(v, children):
    global tree
    # 일단 자기 자리에 값 넣어주기
    tree[v] = numbers[v][1]
    # 루트일때 출력
    if v == 1:
        print('[{}]'.format(tree[v]), end="--")
    # 자식이고 해당층에 자식이 여러개 + 마지막 자식이 아닐때
    elif 1 < v < len(numbers)+1 and len(children) > 1 and v != children[-1]:
        # 내가 자식이 있을때
        if len(numbers[v]) > 2:
            print('+--[{}]'.format(tree[v]), end="--")
        # 없을때
        else:
            print('+--[{}]'.format(tree[v]))
    # 여러자식중 마지막일때
    elif 1 < v < len(numbers)+1 and len(children) > 1 and v == children[-1]:
        # 현재값이 자식을 가질때
        if len(numbers[v]) > 2:
            print(('L--[{}]'.format(tree[v])), end="--")
        else:
            print(('L--[{}]'.format(tree[v])))
    # 자식이 하나
    elif 1 < v < len(numbers)+1 and len(children) == 1:
        # 현재값이 또 자식을 안가질때
        if len(numbers[v]) < 3:
            print('---[{}]'.format(tree[v]))
        else:
            print('---[{}]'.format(tree[v]), end="--")
    # 무자식
    else:
        print()
        return

    # 재귀로 순회하기
    # 현재 노드가 가지는 자식 노드로 보내기
    # 자식 노드가 있는지 검사해주고 반복
    for i in range(2, len(numbers[v])):
        # 길이가 3보다 크면 자식 여러개
        if len(numbers[v]) > 3:
        # 부모노드, 자식 범위 넣어주기
            sol(numbers[v][i], numbers[v][2:])
        # 자식 하나
        elif len(numbers[v]) == 3:
            sol(numbers[v][i], [numbers[v][2]])
        # 무자식
        else:
            sol(numbers[v][i], [0])

sol(1, numbers[1][2:-1])

