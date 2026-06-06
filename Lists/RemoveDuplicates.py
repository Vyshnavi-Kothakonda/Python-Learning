nums = [1, 2, 2, 3, 4, 4, 5]
res = []
for i in nums:
    if i not in res:
        res.append(i)
print(res)
