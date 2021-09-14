import sys
sys.stdin = open("sample_input (h).txt")

t = int(input())
for tc in range(1, t+1):
    n = int(input())

    heap = [0] * (n+1)
    last = 1    # 새로운 노드가 추가 되어야 하는 인덱스(노드번호)

    # 값을 받아와서 heap에 추가하는 함수
    def insert(v):
        global last
        heap[last] = v
        # 2. 새로 추가한 노드의 값이 부모노드 값보다 작으면 바꿔준다.
        c = last
        parent = c // 2
        while parent > 0 and heap[c] < heap[parent]:
            heap[c], heap[parent] = heap[parent], heap[c]
            c = parent
            parent = c // 2

        # 요소를 추가했으니 마지막 요소 위치 변경
        last += 1
    data = list(map(int, input().split()))
    for i in range(len(data)):
        insert(data[i])
    print(heap)
    # 조상 합구하기