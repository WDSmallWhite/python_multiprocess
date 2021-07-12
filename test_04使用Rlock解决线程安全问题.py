import threading
import time

class Account:
	def __init__(self, account_no, balance):
		self.account_no = account_no
		self._balance    = balance
		self.lock       = threading.RLock()

	def getBalance(self):
		return self._balance

	def draw(self, draw_amount):
		self.lock.acquire() #add lock
		try:
			if self._balance >= draw_amount:
				print(threading.current_thread().getName() + " get monety success " + str(draw_amount))
				time.sleep(0.1)
				self._balance -= draw_amount
				print("\tbalance=" + str(account._balance))
			else:
				print(threading.current_thread().getName() + " There is no enough money!")
		finally:
			self.lock.release()

def draw(account, draw_amount):
	account.draw(draw_amount)

def getBalance(account):
	print(threading.current_thread().getName() + " get account money success " + str(account.getBalance()))

if __name__ == '__main__':
	account = Account("12345", 1000)

	threading.Thread(name="A", target=draw, args=(account, 800)).start()
	threading.Thread(name="B", target=draw, args=(account, 800)).start()

	threading.Thread(name="A", target=getBalance, args=(account, )).start()
	threading.Thread(name="B", target=getBalance, args=(account, ))å.start()
			