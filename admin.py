class Admin():

    def __init__(self,FoodID,Food_Name,Quantity,Price,Discount,Stock):
        self.__FoodID = FoodID
        self.__Food_Name = Food_Name
        self.__Quantity = Quantity
        self.__Price = Price
        self.__Discount = Discount
        self.__Stock = Stock

    def __str__(self):
        return f"Food ID : {self.__FoodID} \nFood Name : {self.__Food_Name} \nQuantity : {self.__Quantity} \nPrice : {self.__Price} \nDiscount : {self.__Discount} \nStock Price : {self.__Stock}"

    def set_FoodID(self,FoodID):
        self.__FoodID = FoodID

    def get_FoodID(self):
        return self.__FoodID

    def set_Food_Name(self,Food_Name):
        self.__Food_Name = Food_Name

    def get_Food_Name(self):
        return self.__Food_Name

    def set_Quantity(self,Quantity):
        self.__Quantity = Quantity

    def get_Quantity(self):
        return self.__Quantity

    def set_Price(self,Price):
        self.__Price = Price

    def get_Price(self):
        return self.__Price

    def set_Discount(self,Discount):
        self.__Discount = Discount

    def get_Discount(self):
        return self.__Discount

    def set_Stock(self,Stock):
        self.__Stock = Stock

    def get_Stock(self):
        return self.__Stock
