arr = []
# 添加 append
arr.append(1) # [1]
arr.append(2) # [1,2]

# 删除 del
arr = [1,2,3,4]
del arr[2] # [1,2,4]

# 获取长度 len
arr = [1,2,3,4]
len(arr) # 4

# 组合 +
arr = [1,2,3,4] + [5,6] # [1, 2, 3, 4, 5, 6]

# 重复 *
arr = [1]*4 # [1, 1, 1, 1]

# 包含 in
arr = [1,2,3,4]
print(5 in arr) # False
print(4 in arr) # True

# 遍历 for x in
arr = [1,2,3,4]
for x in arr:
	print(x) # 1 2 3 4