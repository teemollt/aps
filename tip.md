

#### input

1. 반복문으로 여러줄을 입력 받아야 할 때는 `input()`으로 입력 받는다면 시간초과 발생 가능
   - 빠르게 입력 받는법
   - 맨끝에 개행문자가 같이 입력되므로 rstrip()으로 제거

```python
import sys
s = sys.stdin.readline().rstrip()
li = list(map(int, sys.stdin.readline().split().rstrip()))
```

#### 반복문

1. for나 while 내부에서 break으로 멈추지 않고 끝까지 반복을 실행했을 경우 다음 else문을 실행

```python
for i in range(10):
    if i > 10:
        break
else:
    print("haha")
# haha 출력   
```

#### 문자열

1. 아스키코드

   - 변환

     ```python
     # 문자를 아스키코드로
     ord('A')
     # 반대
     chr(65)
     ```

   - 아스키 코드 알파벳 범위 

     - 대문자: 65~90, 소문자: 97~122

2. 문자열탐색

   - 문자열도 in으로 포함여부 알 수 있음 종종 잊어버림..
   
     ```python
     ex = "abc123d"
     if "123" in ex:
         print("O")
     # O    
     ```
   
     

#### 정렬

1. 병합정렬 잘봐두자..

2. sort(), sorted() 구분과 key 사용

   - sort()는 원본을 정렬 a.sort()

   - sorted()는 새리스트에 정렬 sorted(a)

   - 이중리스트일때 정렬기준을 선택해야하는 경우 key사용

     ```python
     arr.sort(key=lambda x: (x[1], x[0]))
     # 2번째요소 1번째 요소 순서로 정렬기준
     ```

3. 중복제거할때 set을 활용하는 방법 외에 다른 방법?

   - 일단은 set을 활용하자

     ```python
     n_arr = list(set(arr))
     # arr-> list
     ```

4. 검색할때 dict를 만들어서 사용하면 빠른 경우가 있음

   - 리스트에만 갇혀있지마...
   - collections 모듈의 Counter 확인 +1

#### 시간복잡도 관련

##### 1.  in 의 시간복잡도

list에 특정 값이 있는지 확인할때  in 의 시간복잡도는 O( n ) 
길이 n의 리스트를 선형으로 순회하므로.

##### 2. 스택, 큐 내용 추가하자

스택 큐 구현시 collections의 deque 활용하면 수행시간 단축 

```python
from collections import deque
dq = deque()
dq.append()
dq.leftpop()
dq.rightpop()
```

