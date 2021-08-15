from sys import stdin
import heapq
input = stdin.readline
n = int(input())
h = []
for i in range(n):
    x = int(input())
    if x:
        heapq.heappush(h, (abs(x), x))
    else:
        if h:
            print(heapq.heappop(h)[1])
        else:
            print(0)