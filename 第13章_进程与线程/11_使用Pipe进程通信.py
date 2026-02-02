import time
from multiprocessing import Process, Pipe


# 子进程1：往队列里放数据
def test1(con1):
    time.sleep(2)
    con1.send('hello')
    print('【test1】发送了 hello')

# 子进程2：从队列里取数据
def test2(con2):
    data = con2.recv()
    print(f'【test2】接收了 {data}')


if __name__ == '__main__':
    con1, con2 = Pipe()

    # 单向管道，con1只能接收，con2只能发送
    # con1, con2 = Pipe(duplex=False)

    p1 = Process(target=test1, args=(con1, ))
    p2 = Process(target=test2, args=(con2, ))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
