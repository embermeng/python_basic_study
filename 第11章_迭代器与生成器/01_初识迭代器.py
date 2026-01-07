# 知识点1：能被 for 循环遍历的对象，就是可迭代对象（iterable）
# region
# names = ['张三', '李四', '王五']
# cities = ('北京', '上海', '深圳')
# msg = 'hello'
#
# age = 10
# def test():
#     pass
#
# for item in test:
#     print(item)
# endregion

# 知识点2：可迭代对象（iterable）都拥有__iter__方法。
# region
# names = ['张三', '李四', '王五']
# cities = ('北京', '上海', '深圳')
# msg = 'hello'
# age = 10
# def test():
#     pass
#
# names.__iter__()
# cities.__iter__()
# msg.__iter__()
#
# print(hasattr(names, '__iter__'))
# print(hasattr(cities, '__iter__'))
# print(hasattr(msg, '__iter__'))
# print(hasattr(age, '__iter__'))
# print(hasattr(test, '__iter__'))
# endregion

# 知识点3：调用__iter__方法会得到：迭代器(iterator)
# region
# 备注1：__iter__是一个魔法方法，当调用iter函数时，__iter__会自动调用。
# 备注2：可迭代对象.__iter__()  等价于： iter(可迭代对象)。
# 备注3：如果iter(obj)能得到一个迭代器(iterator)，那obj就是可迭代对象。

# names = ['张三', '李四', '王五']
# cities = ('北京', '上海', '深圳')
# msg = 'hello'

# print(names.__iter__())
# print(cities.__iter__())
# print(msg.__iter__())

# print(iter(names))
# print(iter(cities))
# print(iter(msg))
# endregion

# 知识点4：迭代器（iterator）拥有__next__方法，每次调用都会根据当前的状态，返回下一个元素。
# region
# 备注1：迭代器.__next__() 等价于  next(迭代器)。
# 备注2：当所有元素全都取出后，若继续调用__next__，Python会抛出StopIteration异常。
# names = ['张三', '李四', '王五']
# it = iter(names)
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# endregion

# for循环的背后逻辑
# region
# names = ['张三', '李四', '王五']
#
# # 1️⃣调用【可迭代对象的__iter__方法】获取到一个迭代器(iterator)
# it  = iter(names)
# # 2️⃣开启一个无限循环
# while True:
#     try:
#         # 3️⃣调用__next__方法，获取下一个元素
#         item = next(it)
#         print(item)
#     except StopIteration:
#         # 4️⃣捕获 StopIteration 异常，随后结束循环
#         break
# endregion

# 知识点5：迭代器（iterator）也拥有__iter__方法，并且其返回值是迭代器自身。
# region
# 这么设计的原因：让 for 循环也能遍历迭代器（即：为了让 iter(迭代器) 不出错）。
# names = ['张三', '李四', '王五']
# it = iter(names)
# print(it)
# print(iter(it))
#
# for item in it:
#     print(item)
# endregion

# 知识点6：迭代器协议：一个对象如果同时满足如下规范，那该对象就是一个迭代器：
# 1. 能被iter()接受。
# 2. 能被next()一步一步取值。
