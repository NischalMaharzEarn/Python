


class bank :
    __bank_name = 'Nischal Bikas Bank Limited' # Bank name static
    __interest_rate = 10 # Interest rate 
    
    def __init__(self,user_first_name,user_second_name,user_current_balance=0): # Defined for user of the bank
        self.user_fname = user_first_name
        self.user_sname = user_second_name
        self.user_balance = user_current_balance
    
    def _check_balance(self):
        return print(f' Your Current Balance is {self.user_balance}')

    def _withdraw_balance(self,withdraw_balance):
        self.user_balance = self.user_balance - withdraw_balance

    def _deposit_balance(self,deposit_balance):
        self.user_balance = self.user_balance + deposit_balance



while True :
    user_input = input (' Press 0 to create account. \n Press 1 to check balance. \n Press 2 to withdraw balance \n Press 3 to deposit balance \n Press 4 to change interest')
    if user_input == '0':
        user_fname = input('Enter User Name')
        user_sname = input('Enter Second Name')
        user_new = bank(user_fname,user_sname)
        print(f'your name is {user_new.user_fname}')
    
    elif user_input == '1':
        user_new._check_balance()
        
    elif user_input == '2':
        deposit_balance = int(input('Enter The Amount You Want To Deposit'))
        user_new._deposit_balance(deposit_balance)
    
    elif user_input == '3':
        withdraw_balance = int(input('Enter The Amount You Want To Withdraw'))
        user_new._withdraw_balance(withdraw_balance)



    


    
    