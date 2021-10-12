#### 최단거리 문제

비용이 모두 양의 정수인 경우 => 다익스트라 O(ElogV) 젤빠름
비용에 음수값이 있는 경우 => 벨만포드 O(EV)
전체를 다 구해야하는 경우 => 플로이드워셜 O(V^3)

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

4. 검색할때 dict를 만들어서 사용하면 빠른 경우가 있음 검색 시간복잡도 O(1)

   - 리스트에만 갇혀있지마...
   - key, value 튜플쌍 dict.items() 사용
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

##### 파라메트릭 서치(이진 탐색)

결정 문제를 최적화 알고리즘으로 변환하는 알고리즘

ex) 계란낙하문제

1~100층의 빌딩에서 계란을 떨어뜨릴때 계란이 깨지지 않는 가장 높은 층 F를 찾는 문제 (단, 계란은 무한함.)

- 가장 단순한 방식: 1층부터 계란이 깨질때까지 한층씩 올라가며 던져보는 방식 => 시간복잡도 O(F)
- 파라메트릭 서치를 이용한 방식
  1. 결정문제 : x층에서 낙하하면 계란이 깨지는지? (isBroken()이라는 함수) 
     => 최적화 알고리즘 : 계란이 깨지지않는 가장 큰 x는 얼마?
  2. 이분법(bisection method) : 수학적으로 방정식의 근을 계산할때 사용한 이진탐색 알고리즘
     => 근이 반드시 존재하는 폐구간에서, 폐구간의 범위를 재귀적으로 좁혀 나감.
  3. 즉, x층에서 낙하하면 계란이 깨지는지 아닌지를 판별하는 함수를 1개 만들고, 깨지지않는 최대층을 찾기위해
     그 함수를 이진탐색으로 돌려보면 됨.

##### 힙 (최대, 최소)

```python
# 힙큐 모듈 사용법 디폴트는 min heap으로 동작
# 최대힙으로 사용하려면 데이터 넣고 꺼낼때 -를 붙여서 사용
# heapq.heappush(heap, item) : item을 heap에 추가
# heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴. 비어 있는 경우 IndexError가 호출됨.
# heapq.heapify(x) : 리스트 x를 즉각적으로 heap으로 변환함 (in linear time, O(N) )
# 튜플로도 푸쉬할수 있음. 팝할때도 튜플로 나옴. 앞쪽 값을 기준으로 삽입
```

##### heapq를 활용한 중간값 구하기

- 좌측에 최대힙 우측에 최대힙 만들고 번갈아가며 값추가하는데, 좌측 루트값보다 우측 루트값이 큰경우 값을 교환해줌
  - priority queue 4번 참고
