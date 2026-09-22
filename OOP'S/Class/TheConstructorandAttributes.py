class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


dog1 = Dog("Buddy", "Golden Retriever")
print(f"{dog1.name} is a {dog1.breed}.")
