import sys
sys.stdin = open("sample_input (bsearch).txt")

def sol(v):
    global tree
    global num
    # 왼쪽
    if 0 < v < n+1:
        sol(v*2)
        # 왼쪽 더이상 없으면 돌아가서 노드값 추가
        tree[v] = num
        # 1부터 1씩 증가시켜가며 넣기
        num += 1
    # 오른쪽
    if 0 < v < n+1:
        sol((v*2)+1)

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    num = 1
    # 최대 노드 번호는 n
    tree = [0] * (n+1)
    sol(1)
    print('#{} {} {}'.format(tc, tree[1], tree[n//2]))