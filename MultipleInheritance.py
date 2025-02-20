class Father:
    def FatherProperty(self):
        print("Father's Property")
        
class Mother:
    def MotherProperty(self):
        print("Mother's Property")
        
class Child(Father,Mother):
    def Property(self):
        print("Child will Inherit: ")
        super().FatherProperty()
        super().MotherProperty()
        
c1 = Child()
c1.Property()