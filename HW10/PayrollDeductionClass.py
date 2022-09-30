class PayrollDeduction:
    def __init__(self,desc,date,amt,num):
        self.__desc = desc
        self.__date = date
        self.__amt = amt
        self.__num = num

    def get_desc(self):
        return self.__desc
    def get_date(self):
        return self.__date
    def get_amt(self):
        return self.__amt       
    def get_num(self):
        return self.__num