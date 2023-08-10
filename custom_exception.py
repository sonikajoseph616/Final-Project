class InvalidAdminLoginError(Exception):

    def __str__(self):
        return "InvalidAdminLoginError : INCORRECT ADMIN NAME AND PASSWORD"
    
class InvalidUserLoginError(Exception):
    
    def __str__(self):
        return "InvalidUserLoginError : INCORRECT USER NAME AND PASSWORD"

class PreviousordersError(Exception):
    
    def __str__(self):
        return "No previous orders"
