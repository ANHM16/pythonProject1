class Person():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print("이름:",self.name)

class client(Person):
    def __init__(self,name,age,gender,asset):
        super().__init__(name,age,gender)
        self.__asset = asset

    def show_asset(self):
        print("자산:",self.__asset)

    def receive(self,owner,money):
        if type(owner) == client:
            self.owner = owner
            owner.__asset = owner.__asset - money
            self.__asset = self.__asset + money
        else:
            raise ValueError("Fuxx off")

class clerk(Person):
    def __init__(self,name,age,gender,bank):
        super().__init__(name,age,gender)
        self.bank = bank

class child(Person):
    def __init__(self,name,age,gender,preschool):
        super().__init__(name,age,gender)
        self.preschool = preschool

Glen = client('Glen',28,'male',10000000)
DJ = client('DJ',25,'male',10000000)
DongHee = child('DongHee',23,'male','Giants')

Glen.receive(DongHee,10000)
Glen.show_asset()