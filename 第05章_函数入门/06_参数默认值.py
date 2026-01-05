# 定义函数，某个形参，一旦设置了默认值，那它后面的所有形参，也必须要写默认值！
def greet(name, gender, age, height, msg='你好'):
    print(f'我叫{name}，性别{gender}，年龄是{age}，身高是{height}')
    print(msg)


# greet('张三', '男', 18, 180)
# greet('张三', '男', 18, 180, 'hello')
# greet('张三', '男', 18, 180, msg='hello')

# print函数底层给end参数设置了默认值
print('尚硅谷', end='!!')