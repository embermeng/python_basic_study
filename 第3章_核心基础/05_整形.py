import sys

age = 18
temp = -15
score = 0

# 当数很大时，可以使用下划线将数字进行分组，来让数字变得更易读
salary = 300_000
house_price = 4_000_000
graduates = 120_000_000

print(salary, house_price, graduates)

a = 9 ** 9999
sys.set_int_max_str_digits(0)
print(a)