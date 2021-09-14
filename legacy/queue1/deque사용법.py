from collections import deque
#deque 데크:앞뒤로 데이터 push pop
arr = list()
#데크 객체 생성 , 리스트를 인자로 넣어줌
dq = deque(arr)
dq.appendleft(1) #데크의 왼쪽에 데이터 삽입
dq.append(2) #데크의 오른쪽에 데이터 삽입
print(dq.pop())   #데크의 오른쪽에서 데이터 pop
print(dq.popleft()) #데크의 왼쪽에서 데이터 pop
####데크를 queue처럼 이용하시려면
#삽입시 append, 삭제시, popleft
####데크를 stack처럼 이용하시려면
#삽입시 append, 삭제시 pop



