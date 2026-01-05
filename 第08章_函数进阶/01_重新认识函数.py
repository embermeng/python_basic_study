# 1️⃣函数也是对象
# a1 = 100  # a1是int类的实例对象
# a2 = 'hello'  # a2是str类的实例对象
# a3 = [10, 20, 30]  # a4是list类的实例对象
#
#
# # welcome函数是function类的实例对象
# def welcome():
#     print('你好啊')
#
#
# print(type(a1))
# print(type(a2))
# print(type(a3))
# print(type(welcome))


# 2️⃣函数可以像对象一样，动态添加属性
# def welcome():
#     print("你好")
#
#
# # 动态添加属性
# welcome.desc = "这是一个用于打招呼的函数"
# welcome.version = 1.0
# print(welcome.__dict__)
# welcome()


# 3️⃣函数可以赋值给变量
# def welcome():
#     print("你好")
#
#
# welcome.desc = "这是一个用于打招呼的函数"
# welcome.version = 1.0
# say_hello = welcome
# say_hello()
# print(say_hello.__dict__)

# 4️⃣可变参数 vs 不可变参数
# 不可变参数
# a = 666
#
#
# def welcome(data):
#     print('data修改前', data, id(data))
#     data = 888
#     print('data修改后', data, id(data))
#
#
# print('函数调用前', a, id(a))
# welcome(a)
# print('函数调用后', a, id(a))

# 可变参数
# a = [10, 20, 30]
#
#
# def welcome(data):
#     print('data修改前', data, id(data))
#     data[2] = 99
#     print('data修改后', data, id(data))
#
#
# print('函数调用前', a, id(a))
# welcome(a)
# print('函数调用后', a, id(a))


# 5️⃣函数也可以作为参数
# def welcome():
#     print("你好")
#
#
# def caller(f):
#     print('caller函数调用了')
#     f()
#
#
# caller(welcome)

# 6️⃣函数也可以作为返回值
# def welcome():
#     print('你好啊！')
#
#     def show_message(msg):
#         print(msg)
#
#     return show_message
#
#
# welcome()('桀桀桀')
