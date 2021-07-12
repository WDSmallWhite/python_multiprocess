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

with ThreadPoolExecutor(max_workers=4) as pool:
    results = pool.map(action, (50, 100, 150)) #启动了三个任务，结果分别保存到results中
    print("----------------")
    for r in results:
        print(r)