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
    
    # 调用三次work函数，得到三个协程对象
    c1 = work(1, 2)
    c2 = work(2, 2)
    c3 = work(3, 2)

    # 等待c1执行完毕
    res1 = await c1
    print('res1:', res1)

    # 等待上面的c1执行完毕后，再等待c2执行完毕
    res2 = await c2
    print('res2:', res2)

    # 等待上面的c2执行完毕后，再等待c3执行完毕
    res3 = await c3
    print('res3:', res3)

    print('main结束', time.time() - start)
    return '我是main的结果'

# 将协程对象交给事件循环
res = asyncio.run(main())
print('res:', res)