import sys
sys.stdin = open("sample_input (nsum).txt")

t = int(input())
for tc in range(1, t+1):
    n, m, l = map(int, input().split())
    tree = [0] * (n+1)
    for i in range(m):
        num, val = map(int, input().split())
        tree[num] = val
    # v : 현재 노드 번호
    def traversal(v):
        if v > n:
            return 0
        # 자식 노드들부터 먼저 순회해서 값 받아오고,
        # 자식노드들의 합을 내 위치에 저장
        left = traversal(v*2)
        right = traversal(v*2+1)
        tree[v] += left+right
        return tree[v]

    traversal(1)
    print('#{} {}'.format(tc, tree[l]))