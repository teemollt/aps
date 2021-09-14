
data= list(map(int,"1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13".split()))
H = 4
MAX_V = pow(2,H+1)
tree = [-1]*(pow(2,H+1))
# 루트는 1
tree[1] = 1
for i in range(0,len(data),2):
    # data[i] : 부모번호
    # data[i+1] : 자식 번호
    parent = data[i]
    child = data[i+1]
    # 자식의 인덱스를 찾아야 함
    # 자식의 인덱스는 : 부모 노드의 인덱스 * 2 또는 부모 인덱스 *2+1
    # 부모노드 인덱스 찾기 :index() 함수 이용
    p_idx = tree.index(parent)
    # 만약에 왼쪽 자식이 없다면, 왼쪽자식에 추가
    # 왼쪽자식이 있다면 오른쪽 자식에 추가
    if tree[p_idx * 2] == -1:   #왼쪽자식이 없음 , 왼쪽 자식으로 추가
        tree[p_idx*2] = child
    else:   #왼쪽 자식이 있으면 오른쪽 자식으로 추가
        tree[p_idx * 2 +1] = child


#부모노드를 기준으로 순회
#전위순회 
#v: 부모노드의 번호
def pre_oreder(v):
    if v >= MAX_V:
        return
    #데이터가 저장되어 있지 않으면 아무작업 하지 않음
    if tree[v] == -1:
        return
    #부모노드부터 처리
    print(tree[v],end=" ")
    #왼쪽노드
    pre_oreder(v*2)
    #오른쪽노드
    pre_oreder(v*2+1)

pre_oreder(1)

#중위순회
#후위순회




