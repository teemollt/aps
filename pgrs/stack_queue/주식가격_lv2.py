def solution(prices):
    answer = []
    n = len(prices)
    for i in range(n):
        cnt = 0
        for j in range(i+1, n):
            if prices[j] >= prices[i]:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)
    return answer

# 스택이나 큐를 활용한 풀이는...