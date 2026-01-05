# 定义函数，/前面只能用『位置参数』，*后面只能用『关键字参数』
def greet(name, /, gender, *, age, height):
    print(f'我叫{name}，性别{gender}，年龄是{age}，身高是{height}')


# 正确示例
greet('张三', '男', age=18, height=180)
greet('张三', gender='男', age=18, height=180)

# 错误示例
greet(name='张三', gender='男', age=18, height=172)
greet('张三', '男', 18, height=172)
