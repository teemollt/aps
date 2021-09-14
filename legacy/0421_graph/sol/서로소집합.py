#서로소 집합
#각 원소의 부모원소를 저장하는 배열
p=[0]   #0번원소는 사용안함
#원소가 1~7까지 존재한다.
for i in range(1,8):
    p.append(i)
#1~7까지 원소는 합집합 연산을 하기 전이기 때문에
#각각 서로소 집합이고, 원소 스스로가 집합의 대표이다.
#서로소 집합들이 실행가능한 연산
# 1. union(x,y) : x 와 y가 포함된 집합을 합하는 연산
# 2. find_set(x): x가 속한 집합의 대표 찾기
def find_set(x):
    #집합의 대표는
    #요소번호와 부모번호가 같은 요소
    if x == p[x]:
        return x
    #아니라면?? 부모를 타고 타고 가서 계속 검색
    return find_set(p[x])

def union(x,y):
    #대표자가 다른 두 개의 요소를 합치는 연산
    a = find_set(x)
    b = find_set(y)
    if a == b:  #이미 같은 집합에 있는 상황
        return
    else:
        #p[b]는 원래 b였음...
        p[b] = a

union(1,2)
union(5,6)
print(p)
print(find_set(6))
union(2,6)
print(find_set(6))
