
#Class relationship
# (1) Aggregation (has a relation) --> one class owns the other class
# example : class customer: has the class address:
# you can not access the private attributes while performing aggrigation

# <>(rombus) --> aggregation

class customer:
    def __init__(self , name , gender , addres):
        self.name = name
        self.gender = gender
        self.address = addres
    def print_address(self):
        print(self.address.get_city() , self.address.pin , self.address.state)
    
    def edit_profile(self , new_name , new_city , new_pin, new_state):
        self.name = new_name
        self.address.edit_address(new_city , new_pin,new_state)



class address:
    def __init__(self,__city ,pin , state):
        self.__city = __city    # private attribute 
        self.pin = pin
        self.state = state

    def get_city(self):
        return self.__city
    
    def edit_address(self ,new_city , new_pin , new_state):
        self.__city = new_city
        self.pin = new_pin
        self.state = new_state


add1 = address('Lucknow','25006','UP')
cust = customer('mohd','male',add1)
print(cust.print_address())

cust.edit_profile('ankit','mumbai',20202 , 'maharastra')
print(cust.print_address())
        
# (2) Inheritance
