import threading
from threading import Thread, Lock
import random
import time

class Bank(Thread):

    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        transaction = 100
        for i in range(transaction):
            random_number = random.randint(50, 500)
            self.balance += random_number
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {random_number}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        transaction = 100
        for i in range(transaction):
            random_number = random.randint(50, 500)
            print(f'Запрос на {random_number}')
            if random_number <= self.balance:
                self.balance -= random_number
                print(f'Снятие: {random_number}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')




