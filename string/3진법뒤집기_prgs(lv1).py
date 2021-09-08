def solution(n):
    t = ''
    answer = 0
    while n:
        t = str(n%3) + t
        n //= 3
    for i in range(len(t)):
        answer += int(t[i])*3**i
    return answer