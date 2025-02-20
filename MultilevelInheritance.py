class GrandParents:
    def PropertyLand(self):
        print("Property Land for Farming given by the GrandParens")
        
class Parents(GrandParents):
    def PropertyHome(self):
        print("Property Home constructed by the parents")
        
class Child(Parents):
    def PropertyVehicle(self):
        print("Property Car Purchased by Child")
        
    def PropertyLand(self):
        print("Property Land from my grandparents is now used for Commercial")
        
c1 = Child()
c1.PropertyLand()
c1.PropertyHome()
c1.PropertyVehicle()

        