def dfs(num, d, n, target, numbers):
    global answer
    if d == n:
        if num == target:
            answer += 1
        return
    dfs(num+numbers[d], d+1, n, target, numbers)
    dfs(num-numbers[d], d+1, n, target, numbers)
answer = 0
def solution(numbers, target):
    n = len(numbers)
    dfs(0, 0, n, target, numbers)
    return answer