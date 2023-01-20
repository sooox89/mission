#ch10
#ex.10-4
class Element():
    def __init__(self,name,symbol,number):
        self.name = name
        self.symbol = symbol
        self.number = number
ob = Element('Hydrogen','H',1)
print(ob.name,ob.symbol,ob.number)