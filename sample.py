class a:
    def __init__(self,name,age):
        self.__name=name
  

    def abc(self):
        print(self.__name)
      

obj=a('ravi',30)
print(obj.__name)
obj.abc()
