

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

   - 

