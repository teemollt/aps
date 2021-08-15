from sys import stdin
import heapq
# 힙큐 모듈 사용법 디폴트는 min heap으로 동작
# 최대힙으로 사용하려면 데이터 넣고 꺼낼때 -를 붙여서 사용
# heapq.heappush(heap, item) : item을 heap에 추가
# heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴. 비어 있는 경우 IndexError가 호출됨.
# heapq.heapify(x) : 리스트 x를 즉각적으로 heap으로 변환함 (in linear time, O(N) )
input = stdin.readline
n = int(input())
h = []
for i in range(n):
    x = int(input())
    if x:
        heapq.heappush(h, -x)
    else:
        if h:
            print(-heapq.heappop(h))
        else:
            print(0)
