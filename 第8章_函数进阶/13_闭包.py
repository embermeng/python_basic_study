def outer():
    num = 10
    print(hex(id(num)))

    def inner():
        nonlocal num
        num += 1
        print(num)

    return inner


f = outer()
f()
f()
f()

# inner把num放到了自己的“小仓库”闭包单元（cell）中
# 仓库中对num增加了一个引用，执行完outer后，内存回收机制不会回收num变量，因为num被引用的次数不为0
# 打印 __closure__ 元组
print(f.__closure__)
# 打印 __closure__ 元组中的某一项
print(f.__closure__[0])
# 打印 __closure__ 元组中的某一项的具体值
print(f.__closure__[0].cell_contents)


# 小案例——文字美化
def beauty(char, n):
    def show_msg(msg):
        print(char * n + msg + char * n)

    return show_msg


show1 = beauty('*', 4)
show1('尚硅谷')
show2 = beauty('@', 5)
show2('尚硅谷')


# 闭包的缺点
# 1. 理解成本较高：对初学者不太友好，滥用会让代码难读。
# 2. 如果闭包里引用了很大的对象，又长期不释放，可能会增加内存占用。
# 3. 很多场景下，其实用【类 + 实例属性】会更清晰，闭包不一定是最优解。

class Beauty:
    def __init__(self, char, n):
        self.char = char
        self.n = n

    def show_msg(self, msg):
        print(self.char * self.n + msg + self.char * self.n)


b1 = Beauty('*', 3)
b1.show_msg('你好啊')
b1.show_msg('尚硅谷')

b2 = Beauty('#', 5)
b2.show_msg('你好啊')
b2.show_msg('尚硅谷')
