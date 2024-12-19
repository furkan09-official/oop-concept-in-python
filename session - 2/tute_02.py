class person:
    def __init__(self , name , country):
        self.name = name
        self.country = country
    
    def greet(self):
        if self.country == 'India':
            return 'Namaste {}'.format(self.name)
        else:
            return 'Hello {}'.format(self.name)

p1 = person('mohd','India')
print(p1.greet())

# pass by reference
def greet(person):
    print('hi! my name is',person.name ,'and i am from',person.country)
# for the first time we are providing the object of class to the function 

p = person('mohd','India')
greet(p)