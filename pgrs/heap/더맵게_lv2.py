import heapq
def solution(scoville, K):
    answer = 0
    s = scoville
    heapq.heapify(s)
    while s[0] < K:
        if len(s) < 2:
            return -1
        heapq.heappush(s, heapq.heappop(s) + heapq.heappop(s)*2)
        answer += 1
    return answer