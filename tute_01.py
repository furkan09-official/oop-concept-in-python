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
            #change pin
            pass
        elif user_input == '3':
            # check balance
            pass
        elif user_input == '4':
            #withdraw
            pass
        else:
            exit()
    def create_pin(self):
        user_pin = input('enter you pin')
        self.pin = user_pin

        user_balance = int(input('enter your balance'))
        self.balance = user_balance
        print('your pin is created successfully')

obj = Atm()
