def greet(name, gender, age, height):
    print(f'我叫{name}，性别{gender}，年龄是{age}，身高是{height}')


# 位置参数
greet('张三', '男', 18, 180)
# 关键字参数
greet(name='张三', gender='男', age=18, height=180)
# 核心优势：参数不挑位置
greet(height=180, age=18, gender='男', name='张三')
# 位置参数和关键字参数混合用，但是位置参数必需在关键字参数前面
greet('张三', '男', height=180, age=18)

# 错误示例
# greet(height=172, age=18, '张三', '男')
# greet(name='张三', '男', 18, 172)
# greet(name='张三', '男', age=18, 172)
# greet(height=172, age=18, gender='男', name='张三', age=19)
# greet(height=172, age=18, gender='男', name='张三', school='尚硅谷')
