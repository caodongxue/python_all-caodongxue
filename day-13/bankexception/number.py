from bankexception.BException import BalanceException
from bankexception.bank import Bank
n=Bank()
try:
    n.takeOut()
except BalanceException as e:
    print(e)