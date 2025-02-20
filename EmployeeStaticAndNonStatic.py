class Employee:
    TotalEmployees = 0
    def __init__(self, empno,empname,salary,deptno):
        self.Empno = empno
        self.Empname = empname
        self.Salary = salary
        self.Deptno = deptno
        Employee.TotalEmployees += 1
        
    def showEmployee(self):
        print(f"Employee No: {self.Empno}\n"
              f"EmpName: {self.Empname}\n"
              f"salary: {self.Salary}\n"
              f"DeptNo: {self.Deptno}") 
        
emp1 = Employee(100,"Punith",200000,8)
emp2 = Employee(101,"Prajwal",50000,8)
print("Total No Employees: ", Employee.TotalEmployees)
emp1.showEmployee()
emp2.showEmployee()