# 문제
# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가
# 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 A, 둘째 줄에 B, 셋째 줄에 C가 주어진다. A, B, C는 모두 100보다 크거나 같고, 1,000보다 작은 자연수이다.
#
# 출력
# 첫째 줄에는 A × B × C의 결과에 0 이 몇 번 쓰였는지 출력한다.
# 마찬가지로 둘째 줄부터 열 번째 줄까지 A × B × C의 결과에 1부터 9까지의 숫자가 각각 몇 번 쓰였는지 차례로 한 줄에 하나씩 출력한다.
num = 1
for i in range(3):
    n = int(input())
    num *= n
num = str(num)
for i in range(10):
    cnt = 0
    for j in num:
        if int(j) == i:
            cnt += 1
    print(cnt)