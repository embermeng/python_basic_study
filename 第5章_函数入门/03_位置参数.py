# 定义函数
def greet(name, gender, age, height):
    print(f'我叫{name}，性别{gender}，年龄是{age}，身高是{height}')

# 位置参数
greet('张三', '男', 18, 180)
# 错误示例
# greet('张三', 18, 180)
# greet('男','张三', 180, 18)