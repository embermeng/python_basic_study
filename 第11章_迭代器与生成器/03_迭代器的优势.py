import tracemalloc
# 1. 迭代器是惰性计算，不会一次性生成所有结果，所以能显著降低内存占用。
# 2. 当数据量很大，不确定要用多少结果时，推荐使用迭代器。

# 使用迭代器实现
class Fibo:
    def __init__(self, total):
        # 要生成多少个数
        self.total = total
        # 当前生成到第几个了（指针）
        self.__index = 0
        # 初识的两个值
        self.pre = 1
        self.cur = 1

    def __iter__(self):
        return self

    def __next__(self):
        # 当生成足够的数量后，抛出StopIteration异常
        if self.__index >= self.total:
            raise StopIteration
        # 前两项都是1
        if self.__index < 2:
            val = 1
        else:
            # 新的结果等于前两项的和
            val = self.pre + self.cur
            # 更新pre和cur
            self.pre = self.cur
            self.cur = val
        # 更新计数器
        self.__index += 1
        return val


# 不用迭代器实现
def fibo(total):
    if total <= 0:
        return []
    if total == 1:
        return [1]
    nums = [1, 1]
    for i in range(2, total):
        nums.append(nums[-1] + nums[-2])
    return nums

# 看内存占用
# tracemalloc.start()
# f1 = Fibo(10000)
# m = tracemalloc.get_traced_memory()[1]
# print(f'内存占用是{m / 1024 / 1024}MB')

# tracemalloc.start()
# f2 = fibo(100000)
# m = tracemalloc.get_traced_memory()[1]
# print(f'内存占用是{m / 1024 / 1024}MB')

f1 = Fibo(10000)
for n in f1:
    if n > 100:
        break
    print(n)

