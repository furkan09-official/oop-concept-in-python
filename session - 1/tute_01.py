print('Welcome to the Oop concept in python class')

class Atm:

    #constructor :  a function inside the class
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()

    
    def menu(self):
        user_input = input("""
        hi how can i help you ?
        1. press 1 to create pin
        2. press 2 to change pi
        3. press 3 to check balance
        4. press 4 to withdraw
        5. press anything to exit
              
        """)
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdraw()
        else:
            exit()
    def create_pin(self):
        user_pin = input('enter you pin')
        self.pin = user_pin

        user_balance = int(input('enter your balance'))
        self.balance = user_balance
        print('your pin is created successfully')
        self.menu()
    def change_pin(self):
        old_pin = input('enter your existing pin')
        if old_pin == self.pin:
            user_pin = input('enter your pin')
            self.pin = user_pin
            print('pin change successfully')
            self.menu()
        else:
            print('not allowed to change the pin')
            self.menu()
    def check_balance(self):
        user_pin = input('enter your pin')
        if user_pin == self.pin:
            print('your balance is :',self.balance)
            self.menu()
        else:
            print('wrong pin entered')
            self.menu()
    def withdraw(self):
        user_pin = input('enter your pin')
        if user_pin == self.pin:
            withdraw_amt = int(input('enter the amount'))
            if withdraw_amt <= self.balance:
                self.balance = self.balance - withdraw_amt
                print('withdraw amount successfully')
                print('current balance is :',self.balance)
                self.menu()
            else:
                print('nikal bhikhari')
                self.menu()
        else:
            print('sale chor')
            self.menu()

obj = Atm()
