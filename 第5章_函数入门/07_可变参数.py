# 可变位置参数、可变关键字参数，可以同时使用，也可以和其他类型的参数一起使用，但必需先写可变位置参数

# 使用*形参名来接收：可变位置参数
def test1(*args):
    # 此处args是元组
    print(args)


# test1('张三', '男', 18, 180)

# 使用**形参名来接收：可变关键字参数
def test2(**kwargs):
    # 此处args是字典
    print(kwargs)


# test2(name="张三", gender="男", age=18, height=180)


# 同时使用：可变位置参数、可变关键字参数
def test3(a, b, *args, c='尚硅谷', **kwargs):
    print('#############################')
    print(f'a:{a}, b:{b}, c:{c}')
    print(args)
    print(kwargs)


test3("张三", "男", '抽烟', '喝酒', age=18, height=180)
