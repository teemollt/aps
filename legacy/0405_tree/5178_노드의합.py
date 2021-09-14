import sys
sys.stdin = open("sample_input (nsum).txt")

t = int(input())
for tc in range(1, t+1):
    # 노드개수 n, 리프노드 개수 m, 출력할 노드번호 l
    n, m, l = map(int, input().split())
    # 트리
    tree = [0] * (n+1)
    # 리프노드 받기
    for i in range(m):
        leaf_i, leaf_v = map(int, input().split())
        tree[leaf_i] = leaf_v
    # 부모노드에 더해주기
    for i in range(n, 1, -1):
        tree[i//2] += tree[i]
    print('#{} {}'.format(tc, tree[l]))