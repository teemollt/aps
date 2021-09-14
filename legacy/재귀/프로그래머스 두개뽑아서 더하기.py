numbers = [1,2,3]

def solution(numbers):
    global used
    answer = []



    return answer

def sol(idx):
    global used
    used[idx] = 1
    for i in range(len(numbers)):
        if i != idx and not used[i]:
            tmp.append(numbers[idx] + numbers[i])
            sol(idx+1)


used = [0] * len(numbers)
print(solution([5,0,2,7]))