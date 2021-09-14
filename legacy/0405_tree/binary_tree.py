class MyBinaryTree:
    # 최대 높이를 받아서 저장할 수 있는 노드의 개수를 지정
    def __init__(self,H):
        self.tree = [0]*(pow(2,H+1))
    #트리에 데이터 추가
    def insert(self,parent,child):
        #만약에 tree안에 parent가 없으면 
        # praent 는 root, child 왼쪽자식
        if parent not in self.tree:
            self.tree[1] = parent
            self.tree[2] = child
        else:   #부모가 tree안에 있으면,
            # child를 tree에 추가 해야 하는데
            # child 의 index를 알아야 함>> 부모의 인덱스를 확인
            p_idx = self.tree.index(parent)
            #child 를 부모의 왼쪽자식으로 등록하거나 오른쪽자식으로 등록
            #왼쪽이 비어 있으면 왼쪽자식 아니면 오른쪽 자식
            if self.tree[p_idx*2] == 0:
                self.tree[p_idx * 2] = child
            else:
                self.tree[p_idx * 2 + 1] = child

    def print_tree(self):
        print(self.tree)
    
    # v : 현재노드의 인덱스
    #전위순회
    def preorder(self,v):
        #좌 우 서브트리를 순회하기 전에, 현재노드에서 작업을 먼저 수행
        print(self.tree[v],end=" ")
        #왼쪽서브트리
        self.preorder(v*2)
        pass
    #중위순회
    def inorder(self,v):
        pass
    #후위순회
    def postorder(self,v):
        pass

data= list(map(int,"1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13".split()))
H = 4
my_tree = MyBinaryTree(H)
for i in range(0,len(data),2):
    my_tree.insert(data[i],data[i+1])

#my_tree.print_tree()


















