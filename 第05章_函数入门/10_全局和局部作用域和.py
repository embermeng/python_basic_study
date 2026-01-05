# 全局作用域 与 局部作用域 以及global的使用
# a = 100
# b = 200
#
# def test():
#     c = '尚硅谷'
#     d = '你好啊'
#     # Python创建一个局部变量a，和全局的a完全不同
#     # a = 300
#
#     # 声明a是全局变量
#     global a
#     a = 300
#     print('函数中的打印a =', a)
#     print('函数中的打印b =', b)
#     print('函数中的打印c =', c)
#     print('函数中的打印d =', d)
# test()
# print('********************')
# print('函数外的打印a =', a)
# print('函数外的打印b =', b)
# print(c)

# 局部作用域 和 局部变量，会在函数调用时创建，在函数执行结束后自动销毁
# def test2():
#     m = 300
#     m += 1
#     print('我是test3中打印的m =', m)
#
#
# test2()
# test2()

# 全局作用域 与 全局变量，会在程序开始时创建，在程序结束后销毁
n = 100
def test3():
    global n
    n += 1
    print('我是test3中打印的n =', n)


test3()
test3()
print('我是全局打印的n =', n)
