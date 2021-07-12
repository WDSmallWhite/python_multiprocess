import threading
import time

class Account:
	def __init__(self, account_no, balance):
		self.account_no = account_no
		self._balance   = balance
		# self.lock       = threading.RLock()
		self.cond       = threading.Condition()
		self._flag      = False 

	def getBalance(self):
		return self._balance

	def depoist(self, despoist_amount):
		self.cond.acquire() 
		try:
			if self._flag:
				self.cond.wait()
			else:
				print(threading.current_thread().getName() + " save monety success " + str(despoist_amount))
				self._balance += despoist_amount
				print("Money = ", self._balance)
				self._flag = True
				self.cond.notify_all()
		finally:
			self.cond.release()

	def draw(self, draw_amount):
		self.cond.acquire() #add lock
		try:
			if not self._flag:
				self.cond.wait()
			else:
				
				print(threading.current_thread().getName() + " get monety success " + str(draw_amount))
				
				self._balance -= draw_amount
				print("\tMoney=" + str(account._balance))
				self._flag = False

				self.cond.notify_all()
				
		finally:
			self.cond.release()

def draw_many(account, draw_amount, max):
	for i in range(max):
		account.draw(draw_amount)

def depoist_many(account, despoist_amount, max):
	for i in range(max):
		account.depoist(despoist_amount)


if __name__ == '__main__':
	account = Account("12345", 0)

	threading.Thread(name="saver", target=depoist_many, args=(account, 800, 2)).start()
	threading.Thread(name="getter", target=draw_many, args=(account, 800, 2)).start()

	threading.Thread(name="saver", target=depoist_many, args=(account, 800, 2)).start()
	threading.Thread(name="getter", target=draw_many, args=(account, 800, 1)).start()
	