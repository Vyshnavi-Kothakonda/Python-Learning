import collections
numbers = [10, 20, 20, 30, 10, 20, 40]
counter = collections.Counter(numbers)
print("Numbers:", numbers)
print("Frequency:", counter)
print("Most Common:", counter.most_common(2))
