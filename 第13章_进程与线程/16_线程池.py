import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import get_native_id, RLock


# 1️⃣创建『线程池执行器』、使用 submit 方法提交任务、使用 shutdown 方法等待任务完成。
# def work(n, lock):
#     with lock:
#         print(f'work正在执行任务{n}......{get_native_id()}')
#     time.sleep(1)
#
#
# if __name__ == '__main__':
#     print('---------start-------------')
#     # 创建一个线程池执行器
#     exec = ThreadPoolExecutor(3)
#     # 创建一个线程锁
#     lock = RLock()
#     # 使用 submit 方法提交任务（submit 只负责“提交任务”，不会阻塞主线程）
#     exec.submit(work, 1, lock)
#     exec.submit(work, 2, lock)
#     exec.submit(work, 3, lock)
#     exec.submit(work, 4, lock)
#     exec.submit(work, 5, lock)
#     exec.submit(work, 6, lock)
#     exec.submit(work, 7, lock)
#
#     # shutdown 的作用：不再接收新的任务。
#     # wait=True 的作用：阻塞主线程，等待线程池中所有任务执行完毕。
#     exec.shutdown(wait=True)
#     print('---------end-------------')

# 2️⃣获取子线程执行后的返回结果（Future类的实例对象 + result方法）
# def work(n, lock):
#     with lock:
#         print(f'work正在执行任务{n}......{get_native_id()}')
#     time.sleep(1)
#     return f'任务{n}的结果'
#
#
# if __name__ == '__main__':
#     print('---------start-------------')
#     # 创建一个线程池执行器
#     exec = ThreadPoolExecutor(3)
#     # 创建一个线程锁
#     lock = RLock()
#     # 使用 submit 方法提交任务（submit 只负责“提交任务”，不会阻塞主线程）
#     futures = [exec.submit(work, index, lock) for index in range(1, 8)]
#
#     # 阻塞主线程，等待线程池中所有任务执行完毕。
#     exec.shutdown(wait=True)
#     # 打印结果
#     for f in futures:
#         print(f.result())
#     print('---------end-------------')

# 3️⃣使用 as_completed：按“完成顺序”获取结果
# def work(n, lock):
#     with lock:
#         print(f'work正在执行任务{n}......{get_native_id()}')
#     if n == 1:
#         time.sleep(15)
#     elif n == 2:
#         time.sleep(10)
#     else:
#         time.sleep(1)
#     return f'任务{n}的结果'
#
# if __name__ == '__main__':
#     print('---------start-------------')
#     # 创建一个线程池执行器
#     exec = ThreadPoolExecutor(3)
#     # 创建一个线程锁
#     lock = RLock()
#     # 使用 submit 方法提交任务（submit 只负责“提交任务”，不会阻塞主线程）
#     futures = [exec.submit(work, index, lock) for index in range(1, 8)]
#     # 收集每个线程返回的结果
#     res_list = []
#     # 保存每个线程返回的结果
#     for f in as_completed(futures):
#         res_list.append(f.result())
#
#
#     # 阻塞主线程，等待线程池中所有任务执行完毕。
#     exec.shutdown(wait=True)
#     # 打印最终的结果
#     print(res_list)
#     print('---------end-------------')

# 4️⃣使用 add_done_callback 方法，为任务添加完成时的回调函数。
# def work(n, lock):
#     with lock:
#         print(f'work正在执行任务{n}......{get_native_id()}')
#     if n == 1:
#         time.sleep(15)
#     elif n == 2:
#         time.sleep(10)
#     else:
#         time.sleep(1)
#     return f'任务{n}的结果'
#
# if __name__ == '__main__':
#     print('---------start-------------')
#     # 创建一个线程池执行器
#     exec = ThreadPoolExecutor(3)
#     # 创建一个线程锁
#     lock = RLock()
#     # 每个线程的执行结果
#     res_list = []
#
#     # 线程执行成功的回调函数
#     def done_func(f):
#         res_list.append(f.result())
#     # 使用submit提交任务，并指定回调函数
#     for index in range(1, 8):
#         f = exec.submit(work, index, lock)
#         f.add_done_callback(done_func)
#
#     # 阻塞主线程，等待线程池中所有任务执行完毕。
#     exec.shutdown(wait=True)
#     # 打印最终的结果
#     print(res_list)
#     print('---------end-------------')

# 5️⃣️使用 map 方法批量提交任务（注意：map方法本身不阻塞，但读取其返回的生成器对象是阻塞的，并且得到结果的顺序，与任务分配的顺序是一致的）
# def work(n, lock):
#     with lock:
#         print(f'work正在执行任务{n}......{get_native_id()}')
#     if n == 1:
#         time.sleep(15)
#     elif n == 2:
#         time.sleep(10)
#     else:
#         time.sleep(1)
#     return f'任务{n}的结果'
#
# if __name__ == '__main__':
#     print('---------start-------------')
#     # 创建一个线程池执行器
#     exec = ThreadPoolExecutor(3)
#     # 创建一个线程锁
#     lock = RLock()
#
#     # 使用map方法批量提交任务
#     res = exec.map(work,range(1, 8), [lock] * 7)
#     # 打印最终的结果
#     print(list(res))
#     # 阻塞主线程，等待线程池中所有任务执行完毕。
#     exec.shutdown(wait=True)
#     print('---------end-------------')

# 6️⃣使用 with：线程池的“自动回收”写法，离开 with 代码块时自动执行 shutdown(wait=True)
def work(n, lock):
    with lock:
        print(f'work正在执行任务{n}......{get_native_id()}')
    if n == 1:
        time.sleep(15)
    elif n == 2:
        time.sleep(10)
    else:
        time.sleep(1)
    return f'任务{n}的结果'

if __name__ == '__main__':
    print('---------start-------------')
    with ThreadPoolExecutor(3) as exec:
        # 创建一个线程锁
        lock = RLock()

        # 使用map方法批量提交任务
        res = exec.map(work,range(1, 8), [lock] * 7)
        # 打印最终的结果
        print(list(res))
    print('---------end-------------')
