from concurrent.futures import ThreadPoolExecutor
import threading
import time

# 任务函数
def action(max):
    my_sum = 0
    for i in range(max):
        my_sum += i
    time.sleep(0.1)
    return my_sum

# 创建线程池，不用关闭
with ThreadPoolExecutor(max_workers=2) as pool:

    # 提交任务
    future1 = pool.submit(action, 50)

    future2 = pool.submit(action, 100)

    # 获取结果
    def get_result(future):
        print(future.result())

    # 线程执行完毕后会自动触发该函数
    future1.add_done_callback(get_result)
    future2.add_done_callback(get_result)

    print("----------------")