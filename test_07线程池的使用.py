from concurrent.futures import ThreadPoolExecutor
import threading
import time

# 定义一个准备作为线程任务的函数
def action(max):
    my_sum = 0
    for i in range(max):
        print(threading.current_thread().name + " " + str(i))
        my_sum += i
    return my_sum

if __name__ == '__main__':
    # 创建一个大小为2的线程池
    pool = ThreadPoolExecutor(max_workers=2)

    # 将任务函数action提交给线程池
    futuer1 = pool.submit(action, 50)

    # 将任务函数action函数提交给线程池
    futuer2 = pool.submit(action, 100)

    # 判断任务1是否结束
    print(futuer1.done())
    time.sleep(3)

    # 查看future1的返回结果,未返回结果时会阻塞。
    print(futuer1.result())

    # 查看future2的返回结果
    print(futuer2.result())

    # 关闭线程池
    pool.shutdown()