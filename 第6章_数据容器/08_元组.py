# 定义有内容的元组
# t1 = (28, 67, 21, 67, 11)
# t2 = ('北京', '尚硅谷', '你好')
# t3 = (100, True, '你好', None)
# t4 = (100, True, '你好', None, (50, 60, 70))
# print(type(t1), t1)  # <class 'tuple'> (28, 67, 21, 67, 11)
# print(type(t2), t2)  # <class 'tuple'> ('北京', '尚硅谷', '你好')
# print(type(t3), t3)  # <class 'tuple'> (100, True, '你好', None)
# print(type(t4), t4)  # <class 'tuple'> (100, True, '你好', None, (50, 60, 70))

# 元组中的元素，不可修改
# t1 = (28, 67, 21, 67, 11)
# t1[0] = 100

# 元组中的元素，不可修改，但元组中如果存放了可变类型（列表），那可变类型中的内容仍可修改
# t2 = (28, 67, 21, 67, 11, [100, 200, 300, ('你好', '尚硅谷')])
# # t2[5] = 400
# t2[5][2] = 400
# # t2[5][3][0] = 'hello'
# print(t2)

# 定义空元组
# t1 = ()
# t2 = tuple()
# print(type(t1), t1)  # <class 'tuple'> ()
# print(type(t2), t2)  # <class 'tuple'> ()

# 定义只有一个元素的元组
# t1 = ('你好',)
# t2 = (18,)
# print(type(t1), t1)  # <class 'tuple'> ('你好',)
# print(type(t2), t2)  # <class 'tuple'> (18,)

# 元组的常用方法
# index 方法：获取指定元素在元组中第一次出现的下标。
# t1 = (28, 67, 21, 67, 11)
# result = t1.index(67)
# print(result)  # 1

# count 方法：统计指定元素在元组中出现的次数。
# t1 = (28, 67, 21, 67, 11)
# result = t1.count(67)
# print(result)  # 2

# 元组的常用内置函数和列表一样，依然是这几个：max、min、len、sorted、sum

# 元组的遍历和列表一样

# 实际开发中的元组，不一定是我们自己定义的，比如函数的可变参数*args就是一个元组
# def demo(*args):
#     return sum(args)
#
# res = demo(100, 200 ,300)
# print(res)