import sys
sys.stdin = open("input (6).txt")

def sol(idx):
    global rst
    # 왼쪽에 노드가 있으면
    if arr[idx][2]:
        # 그쪽으로 가자..
        sol(int(arr[idx][2]))
        # 갔다가 나올때 처리
    rst += arr[idx][1]
    # 오른쪽에 있는지
    if arr[idx][3]:
        sol(int(arr[idx][3]))

for tc in range(1, 11):
    # 정점의 개수 n
    n = int(input())
    # 빈 리스트 준비...
    arr = [[0]*4 for _ in range(n+1)]
    for i in range(n):
        tmp = input().split()
        for j in range(len(tmp)):
            arr[i+1][j] = tmp[j]
    rst = ''
    sol(1)
    print('#{} {}'.format(tc, rst))


