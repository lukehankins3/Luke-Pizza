class Employee:
    def __init__(self, name, num, dept, title, salary):
        self.__name = name
        self.__num = num
        self.__dept = dept
        self.__title = title
        self.__salary = salary

    def get_name(self):
        return self.__name
    def get_num(self):
        return self.__num
    def get_dept(self):
        return self.__dept    
    def get_title(self):
        return self.__title
    def get_salary(self):
        return self.__salary