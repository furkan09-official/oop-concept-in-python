# inheritance : one class(child class) can access  methods, variables from another class(parent class)
# <| (traingle)--> inheritance


# what gets inherited?
# (1) : constructor
# (2) : Non private attributes
# (3) : Non private methods

#parent class
class user:
    def __init__(self):
        self.name = 'mohd'
    
    def login(self):
        print('login')


#child class of the user parent class. means student class can access the user class methods,attributes
class student(user):
    # as i create the object of student class the object can only access the parent class constructor when there is no child 
    # constructor that's why s.name is not printed but when we remove the child class constructor then is would print
    

    # def __init__(self):
    #     self.roll = 100
    
    def enroll(self):
        print('enroll into the course')

u = user()
s = student()
print(s.enroll())    
print(s.login())
print(s.name)



class phone:
    def __init__(self ,price , brand , camera):
        print('inside the constructor')
        self.price = price
        self.brand = brand
        self.camera = camera
    
    def buy(self):
        print('buying a phone')

class smartPhone(phone):
    pass

s = smartPhone(100000,'Apple',14)
s.buy()  # access because it not a private method
#summary : agar chaild ke pass uska khud ka constructor nhi hai to parent ka constructor call ho jayega


class phone:
    def __init__(self ,price , brand , camera):
        print('inside the constructor')
        self.price = price
        self.brand = brand
        self.camera = camera
    
    def buy(self):
        print('buying a phone')

class smartPhone(phone):
    def __init__(self , os , ram):
        self.os = os
        self.ram = ram
        print('inside smartPhone constructor')

s = smartPhone('Android',4)


# child can't access the private member of the class
class phone:
    def __init__(self ,price , brand , camera):
        print('inside the constructor')
        self.__price = price
        self.brand = brand
        self.camera = camera
    
    def show(self):
        print(self.__price)

class smartPhone(phone):
    def check(self):
        print(self.__price)

s = smartPhone(20000,'Apple',14)
print(s.brand)
s.check()
    
