class Bank:

    def __init__(self, balance: List[int]):
        self.accounts = [[i + 1, bal] for i, bal in enumerate(balance)]

        

    def transfer(self, account1: int, account2: int, money: int) -> bool:

        if account1 <= 0 or account2 <= 0 or account1 > len(self.accounts) or account2 > len(self.accounts):
            return False

        #balance
        acc1b = self.accounts[account1 -1][1]
        acc2b = self.accounts[account2 -1][1]

        if money> acc1b:
            return False

        else:
            self.withdraw(account1, money)
            self.deposit(account2, money)
            return True

 

    def deposit(self, account: int, money: int) -> bool:

        if account <= 0 or account > len(self.accounts):
            return False
        

        accountb = self.accounts[account -1][1]
        if money< 0:
            return False
        else:
            self.accounts[account - 1][1] += money 
            return True
  

    def withdraw(self, account: int, money: int) -> bool:

        if account <= 0 or account > len(self.accounts):
            return False

        accountb = self.accounts[account -1][1]

        if money > accountb:
            return False
        else:
            self.accounts[account - 1][1] -= money
            return True
        

        
        
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)