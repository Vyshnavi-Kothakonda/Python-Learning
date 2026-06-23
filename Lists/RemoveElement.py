nums = list(map(int, input().split()))
x = int(input())
while x in nums:
    nums.remove(x)
print(nums)
