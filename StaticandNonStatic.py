class Test:
    staticVariable = 0
    instanceVariable = 0
    def __init__(self):
        print("constructing a object for the Test class")
        self.instanceVariable += 1
        Test.staticVariable += 1
        
t1 = Test()
print("After Creating First Object")
print("Instance variable", t1.instanceVariable)
print("Static Variable:", t1.staticVariable)

t2 = Test()
print("After Creating Second Object")
print("Instance variable", t2.instanceVariable)
print("Static Variable:", t2.staticVariable)
print("Static Variable Using Class Ref: ", Test.staticVariable)