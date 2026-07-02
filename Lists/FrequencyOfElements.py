nums = list(map(int, input().split()))
frequency = {}
for num in nums:
    frequency[num] = frequency.get(num, 0) + 1
print("Element Frequencies:")
for key, value in frequency.items():
    print(key, ":", value)
