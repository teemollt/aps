# import sys
# sys.stdin = open("sample_input (4873).txt")

t = int(input())
for tc in range(1, t+1):
    w = input()
    word = [w[i] for i in range(len(w))]
    stack = []
    while word:
        if not stack:
            stack.append(word.pop(0))
        elif stack[-1] == word[0]:
            word.pop(0)
            stack.pop()
        else:
            stack.append(word.pop(0))

    print('#{} {}'.format(tc, len(stack)))
