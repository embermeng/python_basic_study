name = '张三'
gender = '男'
weight = 75.2
age = 25

# 写法1：直接用加号拼接，很麻烦且很乱，只能是字符串之间拼接
info1 = '我叫' + name + '，我是' + gender + '生' + '，我的体重是'

# 写法2：使用占位符
# %s占位字符串，%f占位浮点数，%i占位整数，%d占位十进制的整数，%s是万能的
# info2 = '我叫%s，我是%s生，我的体重是%f，年龄是%i' % (name, gender, weight, age)
# %s占位符是万能的
info2 = '我叫%s，我是%s生，我的体重是%s，年龄是%s' % (name, gender, weight, age)

# 写法3：使用f-string
info3 = f'我叫{name}，我是{gender}生，我的体重是{weight}，年龄是{age}'