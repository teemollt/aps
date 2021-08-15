import sys, heapq
input = sys.stdin.readline
l, r = [], []
n = int(input())
for i in range(n):
    x = int(input())
    # 양쪽 리스트 길이가 같으면 왼쪽에 최대힙으로 먼저 삽입
    if len(l) == len(r):
        heapq.heappush(r, (-x, x))
    #
    print(l)
