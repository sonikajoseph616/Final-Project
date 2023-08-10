import json
from user import User
from admin_operation import Admin_operations
from custom_exceptions import InvalidUserLoginError,PreviousordersError
class User_operations:
#-----------------------------------------------------------------------------------
    def __init__(self):
        self.Admin_operations = Admin_operations()
        self.personal_details = {}

    # User Register on the application
    def user_registration(self):
        print("\n********* User registration **********")
        Full_Name=input("Enter Full Name : ")
        Phone_Number=input("Enter Phone Number : ")
        self.Email=input("Enter Email : ")
        Address=input("Enter Address : ")
        self.Password=input("Enter Password : ")
        with open("personal_details.json","w") as f:
            json.dump(self.personal_details,f,indent=4)
        print("Successfully register")
        user_obj = User(Full_Name,Phone_Number,self.Email,Address,self.Password)
        user_login_count=1
        while user_login_count<=3:   # User has been provided 3 attempts to log in, if his 3 attempts fail, after that it will stop.
            print("\n********* USER LOG IN **********") # User Login
            entered_Email = input("Enter Email ID : ")
            entered_Password = input("Enter Password : ")
            if self.Email==entered_Email and self.Password==entered_Password:
                print("\n********* Successfully LOG IN **********")
                self.Admin_operations.menu_list_item1()
                self.Admin_operations.menu_list_item2()
                self.Admin_operations.menu_list_item3()
                self.user_choice()
            else:
                try:
                    raise InvalidUserLoginError()
                except Exception as ex:
                    print(ex)
                    print("Please enter correct details.")
                    print(f"{3-user_login_count} attempts left")
                    user_login_count+=1
#-----------------------------------------------------------------------------------
    # User will have the following functionalities:
    def user_choice(self):
        while True:
            user_choice = int(input("Enter \n1.Place New Order \n2.Order History \n3.Update Profile \n4.Log out \nPlease Enter : "))
            if user_choice == 1:
                self.Place_new_order()
        
            elif user_choice == 2:
                self.History()
        
            elif user_choice == 3:
                self.Update_profile()

            elif user_choice == 4:
                print("Log out Successfully")
                break

            else:
                print("Please enter correct choice. ")
#----------------------------------------------------------------------------------
    # Place new order
    history_list=[]
    def Place_new_order(self):
        print("Select your food\n")
        FoodID=int(input("Enter Food ID : "))
        self.Order = self.Admin_operations.search_food_by_ID(FoodID)
        if self.Order:
            print(self.Order)
        self.history_list.append(self.Order)
        print("place an order")
        confirmation = input("Please confirm Yes or No : ")
        if confirmation=="Yes":
            print("Order Placed Successfully\n")
        if confirmation=="No":
            print("Order Cancelled")
#----------------------------------------------------------------------------------
    # previous orders history
    def History(self):
        print("List of all the previous orders history\n")
        if self.history_list:
            for foods in self.history_list:
                print(foods,"\n")
        else:
            print("No previous order found!!")
#----------------------------------------------------------------------------------
    # Update profile
    def Update_profile(self):
        print("\n******* Update user profile *******\n")
        entered_Email = input("Enter Email ID : ")
        entered_Password = input("Enter Password : ")
        if self.Email==entered_Email and self.Password==entered_Password:
            print("\n********* Details Successfully Matched **********\n")

            Full_Name=input("Enter Full Name : ")
            Phone_Number=input("Enter Phone Number : ")
            Email=input("Enter Email : ")
            Address=input("Enter Address : ")
            Password=input("Enter Password : ")

            User.set_Full_Name(self,Full_Name)
            User.set_Phone_Number(self,Phone_Number)
            User.set_Email(self,Email)
            User.set_Address(self,Address)
            User.set_Password(self,Password)
            print("Profile Successfully updated")
            user_obj = User(Full_Name,Phone_Number,Email,Address,Password)
            print(user_obj)

        else:
            try:
                raise InvalidUserLoginError()
            except Exception as ex:
                print(ex)

if __name__=="__main__":
    user=User_operations()
    user.user_registration()
