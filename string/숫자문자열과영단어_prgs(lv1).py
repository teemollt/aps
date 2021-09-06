# 처음 내풀이
def solution(s):
    answer = ""
    tmp = ""
    d = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    for i in s:
        if i.isdigit():
            if tmp in d.keys():
                answer += d[tmp]
                tmp = ""
            answer += i
        else:
            tmp += i
            if tmp in d.keys():
                answer += d[tmp]
                tmp = ""
    answer = int(answer)
    return answer

# replace를 활용하는 것이 훨씬 깔끔함
def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)