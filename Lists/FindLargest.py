nums = list(map(int, input().split()))
largest = nums[0]
for num in nums:
    if num > largest:
        largest = num
print(largest)
