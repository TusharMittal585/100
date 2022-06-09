class atm():
    def __init__(self,atm_card_number,pin_number):
        self.atm_card_number=atm_card_number
        self.pin_number=pin_number
    def cashWithDrawl(self):
        print('Withdrawing cash')
    def CashDeposit(self):
        print('Depositing cash')
    def CheckBalance(self):
        print('Checking balance') 

atm_1=atm('3547282','009') 
print('checking balance')
print('withdrawing cash')

