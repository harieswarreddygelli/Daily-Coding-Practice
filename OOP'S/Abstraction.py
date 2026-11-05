from abc import ABC, abstractmethod

# Inherit from ABC to make it an abstract class
class Abstraction(ABC):
    def __init__(self, age):
        self.age = age

    # Define an abstract method that child classes MUST implement
    @abstractmethod
    def display_details(self):
        pass

# --- HOW IT BEHAVES ---

# 1. You CANNOT create an instance of Abstraction anymore:
# obj = Abstraction(25)  --> Throws TypeError

# 2. You must create a child class that implements the missing method:
class User(Abstraction):
    def display_details(self):
        print(f"User age is: {self.age}")

# 3. You instantiate the child class instead:
user_obj = User(25)
user_obj.display_details()  # Output: User age is: 25
