# 12
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
tree = [0]* 1000
N = int(input())
data = list(map(int,input().split()))
for n in range(N):
    parent,child = data[n*2], data[n*2+1]
    if parent not in tree:
        #현재 부모가 루트
        tree[1] = parent
        tree[2] = child
    else:
        #1. 부모가 저장된 인덱스 찾고
        p_idx = tree.index(parent)
        #2. 부모의 왼쪽부터 자식을 채워넣음
        #   #왼쪽이 있으면 오른쪽에 채워 넣음
        if tree[p_idx*2] == 0:
            tree[p_idx * 2] = child
        else:   #오른쪽 자식에 할당
            tree[p_idx * 2 + 1] = child

print(tree)
#트리 순회하기
#1번부터 순회하면 되는거고
# 자식이 있으면 자식 노드로 이동
# 자식이 있다(현재 index *2 또는 idx*2 +1 위치에 0이 아닌 요소가 있다.

def in_order(idx):
    if tree[idx*2]:
        in_order(idx*2)
    print(tree[idx],end=" ")
    if tree[idx*2+1]:
       in_order(idx * 2 + 1)


def pre_order(idx):
    print(tree[idx],end=" ")
    if tree[idx*2]:
        pre_order(idx*2)
    if tree[idx*2 +1]:
        pre_order(idx * 2 +1)

def post_order(idx):
    if tree[idx * 2]:
        post_order(idx * 2)
    if tree[idx * 2 + 1]:
        post_order(idx * 2 + 1)
    print(tree[idx], end=" ")


pre_order(1)
print()
in_order(1)
print()
post_order(1)
print()



