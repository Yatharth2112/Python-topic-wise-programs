def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print("Arguments:", args)
        print("Keyword Arguments:", kwargs)

        result = func(*args, **kwargs)

        print("Function executed successfully")
        return result

    return wrapper


@logger
def add(a, b):
    return a + b


@logger
def greet(name, age=18):
    print(f"My name is {name} and I am {age} years old.")


print(add(10, 20))
greet("Yatharth", age=18)