class parent:
    def __init__(self,num):
        self.__num = num

    def get_num(self):
        return self.__num
class child(parent):
    def show(self):
        print('this is in child class')

s= child(100)
print(s.get_num())
s.show()