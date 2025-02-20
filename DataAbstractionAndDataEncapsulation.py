class Product:
    def __init__(self):
        self.__productId = ""
        self.__ProductName = ""
        self.__Price = ""
        
    def setProduct(self,pid, pname, price):
        self.__ProductId = pid
        self.__ProductName = pname
        self.__Price = price 
        
    def ShowProduct(self):
        print(f"Product ID: {self.__ProductId}\n"
              f"Product Name: {self.__ProductName}\n"
              f"Price: {self.__Price}\n")
        
    def updateProductPrice(self,price):
        self.__Price = price
        
tv = Product()
tv.setProduct("TV101","LG Golden Eye",18500)
# Try to modify the product name with object it does not change 
tv.__ProductName = "XUV 700"
tv.ShowProduct()
tv.updateProductPrice(20000) # Now it will change
tv.ShowProduct()