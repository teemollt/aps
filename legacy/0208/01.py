# 낙차가 가장 큰 상자의 낙차 구하기
boxes = [7, 4, 2, 0, 0, 6, 0, 7, 0]
# list에서 index로 접근 하는거 연습 --> 고정된 숫자가 아니라 변수로 접근 가능하게

# 1. 첫번재 요소부터 마지막 요소까지 낙차 구하기
#   1-1. 낙차구하기 : 나보다 인덱스가 뒤에 있는 애들중에 나보다 숫자가 작으면 낙차 증가 (끝까지)
# 2. 모든 낙차 중에서 제일 큰 낙차 뽑아내기
# 3. 출력......

max_v = 0
for i in range(len(boxes)):
    cnt = 0
    # 초기화 : 항상 이유가 있는 데이터를 넣어야함.
    for j in range(i+1, len(boxes)):
        # j는 i 보다 뒤쪽에 있는 모든 인덱스
        if boxes[j] < boxes[i]:
            cnt += 1

    if max_v < cnt:
        max_v = cnt

print(max_v)


