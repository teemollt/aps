from sys import stdin
def bs(arr, x):
    pass
n = int(input())
cards = list(map(int, stdin.readline().split()))
card_set = set(cards)
m = int(input())
nums = list(map(int, stdin.readline().split()))
# 딕셔너리로
cards.sort()
d = dict()
for i in range(n):
    if i == 0 or cards[i] != cards[i-1]:
        d[cards[i]] = 1
    else:
        d[cards[i]] += 1
for num in nums:
    if num in card_set:
        print(d[num], end=" ")
    else:
        print(0, end=" ")