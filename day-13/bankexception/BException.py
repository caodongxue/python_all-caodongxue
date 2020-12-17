class BalanceException(Exception):
    def __init__(self,smg):
        self.smg = smg