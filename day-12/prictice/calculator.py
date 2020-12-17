class Calculator:

    def add(self,*args):
        sum=0
        for i in args:
            sum+=i
        print(sum)
        # sum = self.__num + self.__num1
        # print(self.__num,"+",self.__num1,"=",sum)

    def subtract(self,*args):
        sub=args[0]
        for i in args[1:]:
            sub-=i
        print(sub)
        # sub = self.__num - self.__num1
        # print(self.__num,"-",self.__num1,"=",sub)

    def multiply(self,*args):
        mul=1
        for i in args:
            mul*=i
        print(mul)
        # mul = self.__num * self.__num1
        # print(self.__num,"×",self.__num1,"=",mul)

    def divide(self,*args):
        div=args[0]
        for i in args[1:]:
            div/=i
        print(div)
        # div = self.__num / self.__num1
        # print(self.__num,"÷",self.__num1,"=",div)

c=Calculator()
c.add(23,34,56,78)
c.subtract(85,43,23,13,12)
c.multiply(1,2,3,4,5,6)
c.divide(8,2,2)

