def solution(price, money, count):
    answer = -1
    tmp = 0
    for i in range(1, count+1):
        tmp += price * i
    if money > tmp:
        answer = 0
    else:
        answer = tmp - money
    return answer