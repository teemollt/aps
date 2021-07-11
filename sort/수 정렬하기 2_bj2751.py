#  N(1 ≤ N ≤ 1,000,000)
def merge(l, r):
    i = j = 0
    s = []
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            s.append(l[i])
            i += 1
        else:
            s.append(r[j])
            j += 1
    if i == len(l):
        s += r[j:]
    else:
        s += l[i:]
    return s

def msort(arr):
    if len(arr) <= 1:
        return arr
    m = len(arr) // 2
    l = msort(arr[:m])
    r = msort(arr[m:])
    return merge(l, r)

n = int(input())
nums = [int(input()) for _ in range(n)]
for i in msort(nums):
    print(i)