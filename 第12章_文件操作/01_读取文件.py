# Python 中操作文件的标准流程：
# 1. 创建『文件对象』
# 2. 操作文件（读取、写入 等）
# 3. 关闭文件
import time

# 文件操作的核心 —— open函数：它可以打开或创建文件，且支持多种操作模式，返回值是【文件对象】
# open函数最常用的三个参数如下：
# 1. file：要操作的文件路径
# 2. mode：文件的打开模式
#       		r ：读取（默认值）
#       		w ：写入，并先截断文件
#      		    x ：排它性创建，如果文件已存在，则创建失败
#       		a ：打开文件用于写入，如果文件存在，则在文件末尾追加内容
#       		b ：二进制模式
#     		    t ：文本模式（默认值）
#       		+ ：打开用于更新（读取与写入）
# 3. encoding：字符编码

# 读取操作1️⃣：使用『文件对象』的read方法，读取文件中的内容。
# 方法说明：
# 1. read(size)中的size是可选参数。
#      🔸若不传递size参数，表示：读取文件中所有的内容（注意内存占用！）。
#      🔸若传递了size参数，表示：读取文件中指定个数的字符，或指定大小的字节。
# 2. read会从上一次read的位置继续读取，若到达文件末尾后继续读取，将返回空字符串。

# region
# 第一步：创建『文件对象』
# file = open(file='a.txt', mode='rt', encoding='utf-8')
# file = open('a.txt', 'rt', encoding='utf-8')
# file = open('D:/study/python_basic_study/第12章_文件操作/a.txt', 'rt', encoding='utf-8')
# file = open('D:/下载/ssb.zip', 'rb')

# 第二步：操作文件（读取、写入 等）
# 多次调用read去逐步读取文件
# r1 = file.read(2)
# r2 = file.read(3)
# r3 = file.read(4)
# print(r1)
# print(r2)
# print(r3)

# 用循环配合多次read（对内存友好）
# while True:
#     res = file.read(2)
#     if res == '':
#         break
#     print(res)

# 第三步：关闭文件
# file.close()
# endregion

# ......

# ⭐️最佳实践：使用with上下文管理器，结合for循环遍历，逐行读取文件。
with open('a.txt', 'rt', encoding='utf-8') as file:
    for line in file:
        print(line, end='')
