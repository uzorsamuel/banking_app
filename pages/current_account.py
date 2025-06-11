class CurrentAccount(Account):
    def __init__(self, balance):
        Account.__init__(self, balance)

CurrentAccount = CurrentAccount(200000)

CurrentAccount.deposit