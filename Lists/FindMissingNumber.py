n = int(input())
nums = list(map(int, input().split()))
expected_sum = n * (n + 1) // 2
actual_sum = sum(nums)
print("Missing Number:", expected_sum - actual_sum)
