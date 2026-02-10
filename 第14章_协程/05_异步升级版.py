import asyncio
import time

# 定义一个协程函数
async def work(n, delay):
    print(f'work{n}开始')
    print(f'work{n}执行中......')
    # 模拟一个耗时的异步I/O操作
    await asyncio.sleep(delay)
    print(f'work{n}结束')
    return f'工作{n}的结果'

async def main():
    print('main开始')
    start = time.time()
    
    # 把多个协程对象同时丢给事件循环，并在全部执行完后，一次性拿到所有结果。
    results = await asyncio.gather(work(1, 2), work(2, 2), work(3, 2))
    print('results:', results)

    print('main结束', time.time() - start)
    return '我是main的结果'

# 将协程对象交给事件循环
res = asyncio.run(main())
print('res:', res)