''' You only need to code one method - update_seat_count'''

class Route:
    def __init__(self,f,rn,s):
        self.__flightno = f
        self.__route_name = rn
        self.__seats = s
        self.__status = True

    def get_status(self):
        return self.__status


    def update_seat_count(self):
        '''write the code that will reduce the
        number of seats by 1 every time this
        procedure is called. If the seat count
        reaches zero it should change the status 
        attribute to False'''
        if self.__seats == 0:
            self.__status = False
        else:
            self.__seats -= 1
            if self.__seats == 0:
               self.__status = False



class Reservation:
    def __init__(self,p,f,c,s):
        self.__passenger_name = p
        self.__flightno = f
        self.__class = c
        self.__seatno = s

    def get_name(self):
        return self.__passenger_name

    def get_class(self):
        return self.__class
    
    def get_seatno(self):
        return self.__seatno








        





