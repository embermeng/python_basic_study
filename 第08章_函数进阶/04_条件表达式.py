# 条件表达式就是三元表达式、三目运算符

age = 20
# 传统if-else写法
if age >= 18:
    text = '成年'
else:
    text = '未成年'

# 条件表达式写法：结果1 if 条件 else 结果2
text = '成年' if age >= 18 else '未成年'

# 条件表达式的使用场景：简单的二选一场景
rain = True
eat = '外卖' if rain else '出去吃'

is_vip = False
discount = 0.8 if is_vip else 1.0

is_login = False
msg = '欢迎回来！' if is_login else '请先登录！'

print(eat)
print(discount)
print(msg)
