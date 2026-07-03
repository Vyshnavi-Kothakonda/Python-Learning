nums = list(map(int, input().split()))
result = [num for num in nums if num != 0]
zeros = [0] * nums.count(0)
print(result + zeros)
