import threading
import time 

lock = threading.RLock()
class Account:
	def __init__(self, account_no, balance):
		self.account_no = account_no
		self.balance    = balance

def draw(account, draw_amount):
	lock.acquire()
	if account.balance >= draw_amount:
		print(threading.current_thread().getName() + " get monety success " + str(draw_amount))
		time.sleep(0.1)

		#modify balance
		account.balance -= draw_amount
		print("\tbalance=" + str(account.balance))
		

	else:
		print(threading.current_thread().getName() + " There is no enough money!")
	
	lock.release()

if __name__ == '__main__':
	# create an account
	account = Account("1024", 1000)

	
	threading.Thread(name="A", target=draw, args=(account, 800)).start()
	threading.Thread(name="B", target=draw, args=(account, 800)).start()
