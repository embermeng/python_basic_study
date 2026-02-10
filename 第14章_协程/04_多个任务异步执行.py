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
    
    # asyncio.create_task 会把一个协程对象包装成一个可被事件循环调度的任务，并注册到事件循环中
    task1 = asyncio.create_task(work(1, 2))
    task2 = asyncio.create_task(work(2, 2))
    task3 = asyncio.create_task(work(3, 2))

    # 等待task1执行完毕
    res1 = await task1
    print('res1:', res1)

    # 等待上面的task1执行完毕后，再等待task2执行完毕
    res2 = await task2
    print('res2:', res2)

    # 等待上面的task2执行完毕后，再等待task3执行完毕
    res3 = await task3
    print('res3:', res3)

    print('main结束', time.time() - start)
    return '我是main的结果'

# 将协程对象交给事件循环
res = asyncio.run(main())
print('res:', res)