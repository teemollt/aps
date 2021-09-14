import sys
sys.stdin = open("sample_input (4881).txt")
# idx : 행을 의미하는 인덱스
# sum_v : 값을 선택했을 때 누적합
def solve(idx, used, sum_v):
    global min_v
    # 경우의 수를 줄이기 위해서, 유망하지 않으면 실행하지 않음(백트래킹)
    if sum_v >= min_v:
        return
    # idx 랑 n이랑 같아지면 모든행을 다 결정했다는 뜻.
    if idx == n:
        # 다결정하고 아무것도 안해도됨.
        if sum_v < min_v:
            min_v = sum_v
        return
    # 각 행에서 선택할 수 있는 열을 선택한다음
    # 다음행을 결정한다.
    for i in range(n):  # 각 열을 확인
        if not used[i]: # used[i] == 0 아직 사용하지 않은 열
            # 각각 인덱스가 필요한게 아니라 합만 알면됨
            # 각 행에서 열을 선택할 때마다, 열의 값을 더해서
            # 다음 행으로 넘어감
            used[i] = 1    # i번 열 사용표시
            solve(idx+1, used, sum_v + data[idx][i])
            # i번 열을 선택했을때, 경우의 수를 모두 고려했으니
            # 다음 연산을 위해 다시 리셋
            used[i] = 0

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    used = [0] * n   # 순열을 만드는데 사용된 선택된 열을 표시하기 위한 배열 visited같은거..
    # 순열 만들어서 합구하기
    min_v = 100         # 100을 넘을 수 없으므로 100으로 초기화
    solve(0, used, 0)   # sum_v 0으로 초기화
    print('#{} {}'.format(tc, min_v))