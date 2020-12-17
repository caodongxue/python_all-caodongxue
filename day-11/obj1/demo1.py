class Car:
    __brand = None

    def setBrand(self,b):
        self.__brand = b

    def getBrand(self):
        return self.__brand

c = Car()
c.setBrand("大众辉腾")
name = c.getBrand()
print(name)
print(c)
