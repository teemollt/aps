import sys
sys.stdin = open("sample_input (4).txt")
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    a = list(map(int, input().split()))
    # 정렬
    for i in range(len(a)):
        min = i
        for j in range(len(a)):
            if a[min] > a[j]:
                min = j
                a[i], a[min] = a[min], a[i]
    # 리스트에 순서대로 추가
    rst = []
    for i in range(len(a)):
        rst.append(a[i])
        rst.append(a[len(a)-1-i])
    print('#{}'.format(tc), end=" ")
    for i in range(10):
        print(rst[i], end=" ")
    print()

