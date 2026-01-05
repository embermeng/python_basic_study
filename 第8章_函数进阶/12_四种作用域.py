# 内建作用域把py文件包起来了
# 全局作用域
a = 100
def test(b):
    # 外层作用域
    print('我是test函数，test中打印的a是', a)
    print('test收到的参数b是', b)
    c = 200
    d = 300
    print('test中的c和d是', c, d)

    def inner():
        # 局部作用域
        e = 400
        nonlocal c
        c = 999
        print('inner中的e是', e)
        print('inner中打印的c是', c)
        print('@@@@@@@', a)
    inner()
    print('test中的c是', c)

print('全局打印的a是', a)
test(66)

print(print)