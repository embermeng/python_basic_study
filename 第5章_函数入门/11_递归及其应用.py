# n从大到小
# def welcome(n):
#     print(f'你好啊{n}')
#     # 递归要有结束条件
#     if n > 1:
#         welcome(n - 1)


# n从小到大
# def welcome(n):
#     # 递归要有结束条件
#     if n > 1:
#         welcome(n - 1)
#     print(f'你好啊{n}')

# welcome(5)

# 递归的应用：使用递归完成一个数的阶乘
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


res = factorial(5)
print(res)
