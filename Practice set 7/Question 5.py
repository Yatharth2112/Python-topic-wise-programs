class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return (f"Title by Author {self.name}")
        
    def __len__(self):
        return len(self.name)

obj1 = Book("Harry")
print(obj1)  
print(len(obj1))

obj2 = Book("Yatharth")
print(obj2)
print(len(obj2))
