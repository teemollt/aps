import sys
sys.stdin = open("GNS_test_input.txt")

def search(numbers, word):
    for i in numbers:
        if i == word:
            rst.append(i)
    return rst

t = int(input())
for tc in range(1, t+1):
    x, n = input().split()
    n = int(n)
    num = list(input().split())
    w = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    rst = []
    for i in w:
        search(num, i)

    print('#{}'.format(tc))
    for i in rst:
        print(i, end=" ")
    print()
