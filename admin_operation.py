from admin import Admin
import random
from custom_exceptions import InvalidAdminLoginError
class Admin_operations:
#-----------------------------------------------------------------------------------
    Food_Items_list = []       # static variable

    #The application will have a log-in for admin
    def admin_login(self):
        admin_id="Admin"
        admin_password="Pass@123"
        # Ask for Admin ID and password for login
        admin_login_count=1
        while admin_login_count<=3:     # Admin has been provided 3 attempts to log in, if his 3 attempts fail, after that it will stop.
            print("\n********* ADMIN LOG IN **********")
            entered_admin_id=input("Enter admin id : ")
            entered_admin_password=input("Enter admin password : ")
            if admin_id==entered_admin_id and admin_password==entered_admin_password:
                print("\n********* LOG IN Successfully **********")
                self.menu_list_item1()
                self.menu_list_item2()
                self.menu_list_item3()
                self.admin_choice()
            else:
                try:
                    raise InvalidAdminLoginError()
                except Exception as ex:
                    print(ex)
                    print("Please enter correct details.")
                    print(f"{3-admin_login_count} attempts left")
                    admin_login_count+=1
#-----------------------------------------------------------------------------------
    # Admin will have the following functionalities:
    def admin_choice(self):
        while True:
            admin_choice = int(input("1.Add Items \n2.Edit Items \n3.View Items \n4.Remove Items \n5.Log out \nPlease Enter : "))
            if admin_choice == 1:
                self.add_items()
        
            elif admin_choice == 2:
                self.edit_items()
        
            elif admin_choice == 3:
                self.view_items()

            elif admin_choice == 4:
                self.remove_items()

            elif admin_choice == 5:
                print("Log out Successfully")
                break

            else:
                print("Please enter correct choice. ")
#-----------------------------------------------------------------------------------
    # menu_list_item1
    def menu_list_item1(self):
        print("\n********* Menu List **********")
        FoodID= FoodID = random.randint(1, 999)
        Food_Name="Tandoori Chicken"
        Quantity="4 pieces"
        Price=240.0
        Discount=20.0
        Stock=7000.0
        admin_obj = Admin(FoodID,Food_Name,Quantity,Price,Discount,Stock)
        Admin_operations.Food_Items_list.append(admin_obj)
#-----------------------------------------------------------------------------------
# menu_list_item2
    def menu_list_item2(self):
        FoodID= FoodID = random.randint(1, 999)
        Food_Name="Vegan Burger"
        Quantity="1 piece"
        Price=320.0
        Discount=30.0
        Stock=5000.0
        admin_obj = Admin(FoodID,Food_Name,Quantity,Price,Discount,Stock)
        Admin_operations.Food_Items_list.append(admin_obj)
#-----------------------------------------------------------------------------------
# menu_list_item3
    def menu_list_item3(self):
        FoodID= FoodID = random.randint(1, 999)
        Food_Name="Truffle Cake"
        Quantity="500gm"
        Price=900.0
        Discount=50.0
        Stock=2000.0
        admin_obj = Admin(FoodID,Food_Name,Quantity,Price,Discount,Stock)
        Admin_operations.Food_Items_list.append(admin_obj)
        for foods in self.Food_Items_list:
            print(foods,"\n")
#-----------------------------------------------------------------------------------
    # Add new Items
    def add_items(self):
        print("\n********* Add Items **********")
        FoodID=int(input("Enter Food Id : "))
        Food_Name=input("Enter Food Name : ")
        Quantity=input("Enter Food Quantity : ")
        Price=float(input("Enter Food Price : "))
        Discount=float(input("Enter Food Discount : "))
        Stock=float(input("Enter Food Stock : "))
        admin_obj = Admin(FoodID,Food_Name,Quantity,Price,Discount,Stock)
        self.Food_Items_list.append(admin_obj)
        print("Successfully Added")
#-----------------------------------------------------------------------------------
    # (Reusable method) Search Food Item By ID for performing Edit and Remove operations.
    def search_food_by_ID(self,FoodID):
        for foods in self.Food_Items_list:
            if foods.get_FoodID() == FoodID:
                return foods
        print("No such Food ID Found!!")
#-----------------------------------------------------------------------------------
    # Edit Food Items
    def edit_items(self):
        print("\n******* Edit Food Items *******")
        FoodID = int(input("Enter Food Id : "))
        Admin = self.search_food_by_ID(FoodID)
        if Admin:
            Food_Name = input("Enter Food Name : ")
            Quantity = input("Enter Food Quantity : ")
            Price = float(input("Enter Food Price : "))
            Discount = float(input("Enter Food Discount : "))
            Stock = float(input("Enter Food Stock : "))

            Admin.set_Food_Name(Food_Name)
            Admin.set_Quantity(Quantity)
            Admin.set_Price(Price)
            Admin.set_Discount(Discount)
            Admin.set_Stock(Stock)
            print("Food Item Successfully Updated")
#-----------------------------------------------------------------------------------
    # View the list of Food Items
    def view_items(self):
        print("\n********* List of all Food Items *******")
        for foods in self.Food_Items_list:
            print(foods,"\n")
#-----------------------------------------------------------------------------------
    # Delete a food item
    def remove_items(self):
        print("\n******* Remove Food Items from list ******")
        FoodID = int(input("Enter Food ID : "))
        Admin = self.search_food_by_ID(FoodID)
        if Admin:
            self.Food_Items_list.remove(Admin)
            print("Item Successfully Removed")
if __name__=="__main__":
    admin=Admin_operations()
    admin.admin_login()
