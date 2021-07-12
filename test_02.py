import threading
import time
def action(num):
	for i in range(num):
		print(threading.current_thread().getName() + " " +str(i))
		time.sleep(1)


if __name__ == '__main__':
	for i in range(100):
		if i == 20:
			t1 = threading.Thread(target=action, args=(10, ))
			t1.start()

			t2 = threading.Thread(target=action, args=(10, ))
			t2.start()

			t1.join(1)
			t2.join(1)

		print(threading.current_thread().getName() + " " + str(i))
