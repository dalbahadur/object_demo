class Calculate:
    def Sum(self,first,second,third,four):
        self.__first=first
        self.__second=second
        self.__third=third
        self.__four=four
        total=first+second+third+four
        return total
    def Mul(self,first,second,third,four):
        self.__first=first
        self.__second=second
        self.__third=third
        self.__four=four
        total=first*second*third*four
        return total

    def Sub(self,first,second,third,four):
        self.__first=first
        self.__second=second
        self.__third=third
        self.__four=four
        total=(first-second)-(third-four)
        return total
