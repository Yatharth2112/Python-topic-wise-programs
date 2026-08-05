class MathUtils:
    def __init__(self,a,b):
        pass

    @staticmethod
    def add(a,b):
        return a + b

    @classmethod
    def description(cls):
        print("This is a utility class for math operations.")
        
obj1 = MathUtils
print(obj1.add(6, 3))
obj1.description()
print("This is done by creating an object")
print(MathUtils.add(6,4))
MathUtils.description()    
print("This is done without creating an object")        