def grade(n):
    if n >= 90:
        return "A"
    elif n >= 80:
        return "B"
    elif n >= 70:
        return "C"
    elif n >= 50:
        return "D"
    else:
        return "F"

def solution(scores):
    answer = ''
    n = len(scores)
    arr = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            arr[i][j] = scores[j][i]
        if arr[i][i] == max(arr[i]) and arr[i].count(arr[i][i])==1:
            answer += grade((sum(arr[i])-arr[i][i])/(n-1))
        elif arr[i][i] == min(arr[i]) and arr[i].count(arr[i][i])==1:
            answer += grade((sum(arr[i])-arr[i][i])/(n-1))
        else:
            answer += grade(sum(arr[i])/n)
    return answer