import threading
import time
import queue

# define a product function
def product(bq):
	str_tuple = ("Python", "C++", "JAVA")
	for i in range(9999):
		# print(threading.current_thread().name + "producter is producting an element!")
		time.sleep(0.2)

		bq.put(str_tuple[i % 3])

		print(threading.current_thread().name + "producter producted an element!")

def consume(bq):
	while True:
		# print(threading.current_thread().name + "consumer is consuming an element!")
		time.sleep(0.2)

		t = bq.get() #get ele form queue

		print(threading.current_thread().name + "consumer consumed an element!")


if __name__ == '__main__':
	bq = queue.Queue(1)
	threading.Thread(target=product, args=(bq, )).start()
	threading.Thread(target=product, args=(bq, )).start()
	threading.Thread(target=product, args=(bq, )).start()
	
	threading.Thread(target=consume, args=(bq, )).start()


