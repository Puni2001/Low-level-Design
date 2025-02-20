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
        
class SalesMan(Employee):
    def __init__(self,empno, empname,salary,deptno,comm):
        self.Commission = comm
        # invoke the members of base class  from derived class we use super()
        super().__init__(empno, empname,salary,deptno)
        
emp1 = SalesMan(101,"Punith",100000,10,500)
emp1.showEmployee()
print("Commission:",emp1.Commission)
        
        