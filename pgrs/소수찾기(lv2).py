# 소수판별할때 해당 숫자의 제곱근까지만 확인해봐도됨
def checkP(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
# 완탐
def sol(s, d, n, numbers, used):
    global li
    if s and checkP(int(s)):
        li.append(int(s))
    if d == n:
        return
    for i in range(n):
        if numbers[i] and not used[i]:
            used[i] = 1
            sol(s+numbers[i], d+1, n, numbers, used)
            used[i] = 0
li = []
def solution(numbers):
    n = len(numbers)
    used = [0]*n
    sol('', 0, n, numbers, used)
    answer = len(list(set(li)))
    return answer