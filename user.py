class User():

    def __init__(self,Full_Name,Phone_Number,Email,Address,Password):
        self.__Full_Name = Full_Name
        self.__Phone_Number = Phone_Number
        self.__Email = Email
        self.__Address = Address
        self.__Password = Password

    def __str__(self):
        return f"Full Name : {self.__Full_Name} \nPhone Number : {self.__Phone_Number} \nEmail : {self.__Email} \nAddress : {self.__Address} \nPassword : {self.__Password}"

    def set_Full_Name(self,Full_Name):
        self.__Full_Name = Full_Name

    def get_Full_Name(self):
        return self.__Full_Name

    def set_Phone_Number(self,Phone_Number):
        self.__Phone_Number = Phone_Number

    def get_Phone_Number(self):
        return self.__Phone_Number

    def set_Email(self,Email):
        self.__Email = Email

    def get_Email(self):
        return self.__Email

    def set_Address(self,Address):
        self.__Address = Address

    def get_Address(self):
        return self.__Address

    def set_Password(self,Password):
        self.__Password = Password

    def get_Password(self):
        return self.__Password
