import functools, password_stuff

print("password_stuff", __name__)


login = {
    "Login": "Mollie", "access_level": "admin", 
    "Login": "Kyle", "access_level": "admin",
    "Login": "Brady", "access_level": "guest",  
    }


class MT_Bookshelf:
    if login in login == "Mollie":
        print("Welcome, Mollie!")

        
        
    def __init__(self, name: str, pages: int, rating: int):
        self.name = name 
        self.pages = pages
        self.rating = rating

    def __str__(self, *pages, rating):
        return (
            f"<Book {self.name}, read {self.pages} pages, rated {self.rating} out of 100>"
        )
    def my_decorator(self):
        @wrap 
        def wrapper(*args, **kwargs):
            print("Decorated function goes here.") # this isnt implemented yet, but its a rough idea
        return f(*args, **kwargs)

      
    
    
class KT_Bookshelf(self, name, pages: int, rating: int):
    if login in login == "Kyle":
        print("Welcome Kyle!")

    def my_decorator(self):
        

    def __init__(self):
        self.name = name 
        self.pages = pages
        self.rating = rating
    
    def __str__(self, *pages, rating):
        return (
            f"<Book {self.name}, read {self.pages} pages, rated {self.rating} out of 100"
        )

print()