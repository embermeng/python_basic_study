# None 是一个特殊的字面量，用来表示：空值、无值、无意义
msg = None

# None的类型是NoneType
print(type(msg))

# None转为布尔值是False
print(bool(msg))

# None不能参与任何数学运算，也不能与字符串拼接
# res1 = msg + 1
# res1 = msg + 'hello'