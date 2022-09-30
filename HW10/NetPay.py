import EmployeeClass as e
import PayrollDeductionClass as p

def main():
    employee = create_employee()
    deductions = enter_deductions()
    show_NetPay(employee,deductions)

def create_employee():
    name = 'Jimmy'
    num = 58475
    dept = 'Information Systems'
    title = 'Developer'
    salary = 6800.00
    
    employee = e.Employee(name,num,dept,title,salary)
    return employee


def enter_deductions():
    deduction1 = p.PayrollDeduction('food court','8/14/2022',22.50,39119)
    deduction2 = p.PayrollDeduction('gift contribution','8/12/2022',25.00,58475)
    deduction3 = p.PayrollDeduction('food court','8/17/2022',15.25,21547)
    deduction4 = p.PayrollDeduction('vending machine','8/22/2022',3.00,58475)
    deduction5 = p.PayrollDeduction('vending machine','8/5/2022',2.75,58745)
    deductions = [deduction1, deduction2, deduction3, deduction4, deduction5]

    return deductions


def show_NetPay(employee, deductions):

    
    if e.Employee.get_num == p.PayrollDeduction.get_num:
        deduct = sum(p.amt)






    print("*** Employee Pay ***")
    print("Name: ", e.Employee.get_name(employee))
    print("ID Number: ", e.Employee.get_num(employee))
    print("Department: ", e.Employee.get_dept(employee))
    print("Gross Pay: ", e.Employee.get_salary(employee))
    print("Net Pay: ", (float(e.Employee.get_salary(employee)) - float(deduct)))


main()

