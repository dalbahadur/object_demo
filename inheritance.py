class Vechical:
    def __init__(self,name,model,color):
        self._car_name=name
        self._car_model=model
        self._car_color=color

    def start(self,n,c,b,g):
        self.__vechical_newtol=n
        self.__vechical_cloch=c
        self.__vechical_brake=b
        self.__vechical_gear=g

        if(self.__vechical_newtol=='false'):
            print("The vechical is in stop)
        else:
            print("The vechical is start mode")



class Car:
    pass



