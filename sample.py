class a:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def abc(self):
        print(self.__name)
        print(self.__age)

obj=a('ravi',30)
print(obj.__name)
obj.abc()
