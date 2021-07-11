n = int(input())
nums = [int(input()) for _ in range(n)]
# selection
for i in range(n):
    min_i = i
    for j in range(i+1, n):
        if nums[j] < nums[min_i]:
            min_i = j
    nums[min_i], nums[i] = nums[i], nums[min_i]
for i in nums:
    print(i)
