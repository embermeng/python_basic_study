# filter函数：从一组数据中，筛选出符合条件的元素（过滤），并组成一组新数据。
# 语法格式：filter(过滤函数, 可迭代对象)

# 筛选数值
nums = [10, 20, 30, 40, 50]
res = filter(lambda n: n > 30, nums)
print(list(res))

# 筛选成年人
persons = [
    {'name': '张三', 'age': 15, 'gender': '男'},
    {'name': 'Tom', 'age': 18, 'gender': '男'},
    {'name': 'Jerry', 'age': 17, 'gender': '男'},
    {'name': '李华', 'age': 20, 'gender': '女'},
    {'name': '赵六', 'age': 40, 'gender': '男'},
    {'name': '孙七', 'age': 17, 'gender': '女'},
]
res = filter(lambda p: p['age'] >= 18, persons)
print(list(res))

# 过滤非法字符串
names = ['张三', '', '李四', None, '王五', True]
res = filter(lambda name: name, names)
print(list(res))

# 注意点
# 1.延迟执行：filter不会立刻筛选，只有在“需要结果”时才执行。
# 2.返回的是迭代器对象，且一旦遍历完成就会被“耗尽”。
# 3.filter可能会影响元素数量。

# filter函数的特殊用法：如果不传递过滤函数，那么自动会过滤掉“假值”
data = [0, 1, '', 'hello', [], (), 5]
result = filter(None, data)
print(list(result))


