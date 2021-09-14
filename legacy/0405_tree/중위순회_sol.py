# v: 현재 노드의 번호
def inorder(v):
    if v <= max_num and tree[v]:
        # 왼쪽 현재 오른쪽
        inorder(left[v])
        print(tree[v], end="")
        inorder(right[v])

for tc in range(1, 11):
    n = int(input())
    max_num = pow(2, n)
    tree = [0]*(max_num+1)
    # n은 노드의 개수만 의미하고 노드번호는 트리 인덱스와 동일한 번호 가짐
    left = [0]*(max_num+1)
    right = [0]*(max_num+1)
    for i in range(n):
        data = list(input().split())
        

