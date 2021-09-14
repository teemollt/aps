import sys
sys.stdin = open("input (hw).txt")

def dfs(a):
    visited[a] = 1
    route.append(a)

    if arr1[a] and visited[arr1[a]] == 0:
        dfs(arr1[a])
    if arr2[a] and visited[arr2[a]] == 0:
        dfs(arr2[a])



while True:
    try:
        tc, line = map(int, input().split())
        # 한 지점당 두곳으로만 갈수있므로 두개의 배열 생성
        arr1 = [0] * 100
        arr2 = [0] * 100
        # 지점 인풋
        point = list(map(int, input().split()))
        # 0~point 끝까지 짝수번째마다 출발점이므로 2씩 점프하며 반복문
        for i in range(0, len(point), 2):
            # 배열에 넣기위해 0~99중 출발점이 무엇인지 검색
            for j in range(100):
                # 만약 출발점인 point[i]가 j와 같다면
                if point[i] == j:
                    # 출발점이 j라는 뜻, 그런데 arr1 해당 인덱스에 이미 값이 들어있다면 arr2에 해당값 저장
                    # 해당값은 도착점이고 도착점은 point[i+1]
                    if arr1[j]:
                        arr2[j] = point[i+1]
                    else:
                        arr1[j] = point[i+1]
        # print(tc, line)
        # print(arr1)
        # print(arr2)
        visited = [0] * 100
        route = []
        rst = 0
        dfs(0)
        if 99 in route:
            rst = 1
        print('#{} {}'.format(tc, rst))
    except:
        break