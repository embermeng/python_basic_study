# map函数：对一组数据中的每一个元素，统一执行某种操作（加工），并生成一组新数据。
# 语法格式：map(操作函数, 可迭代对象)

# 统一数据处理
# map函数的返回值是一个迭代器对象（类型和传入的迭代对象相同），需要我们自己去手动遍历，或者手动类型转换
nums = [10, 20, 30, 40]
res = map(lambda x: x * 2, nums)
print(list(res))
print(nums)

# 字符串转换
names = ('python', 'java', 'js')
res = map(lambda x: x.upper(), names)
print(tuple(res))
print(names)

# 类型转换
strNum = {'1', '2', '3'}
res = map(int, strNum)
print(set(res))
print(strNum)

# 注意点：
# 1.延迟执行：map 不会立刻计算，只有在“需要结果”时才执行计算。
# 2.返回的是迭代器对象，且一旦遍历完成，就会被“耗尽”。
# 3.map不会影响元素数量。
nums = [10, 20, 30, 40]
res = map(lambda x: x * 2, nums)
nums2 = list(res)
print(list(res))  # res变成[]，被“耗尽”了
print(nums2) # 但是nums2把结果保存了
print(nums2)


