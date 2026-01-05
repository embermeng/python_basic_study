# 二进制（binary），b可大写
num1 = 0b11001
# 八进制（octal），o可大写
num2 = 0o1044
# 十六进制（hexadecimal），x可大写
num3 = 0x1cf

# Python中所有的非十进制数字，只是代码层面的编写方式，是给程序员看的
# Python在进行：计算、打印等操作时，会自动将这些『非十进制』数字，转为『十进制』数字。
# print(num1, num2, num3)
# print(num1 + 1)
# print(str(num2))
# print(num3 > 400)

# bin()将十进制转为二进制的字符串
res1 = bin(25)
# oct()将十进制转为八进制的字符串
res2 = oct(548)
# hex()将十进制转为十六进制的字符串
res3 = hex(463)
# print(res1, res2, res3)

# 使用int()将制定进制的数（字符串形式）转为十进制数字
val1 = int('0b11001', 2)
val2 = int('0o1044', 8)
val3 = int('0x1cf', 16)
# print(val1, val2, val3)